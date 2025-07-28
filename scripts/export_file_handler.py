import re


import pandas as pd
import scripts.df_handler as dfh
from utils.utils import Utils

class ExportFileHandler:
    def __init__(self, dataframe:pd.DataFrame = None ,selected_columns:list = [], table_name:str = "",db_name:str="SNOWFLAKE",selected_case:str="UPPER"):
        if dataframe is None or dataframe.shape[0] == 0:
            raise ValueError("Dataframe is empty")
        if len(selected_columns) == 0:
            raise ValueError("Please select at least one column")
        if table_name == "":
            raise ValueError("Table name could not be empty")

        self._dfh = dfh.DFHandler(dataframe)
        self._selected_columns = selected_columns
        self._table_name = table_name
        self._db = db_name
        self._col_sql_dtype_map = dict()
        self._selected_case = selected_case.upper()
        for col_name,dtype in self._dfh.get_column_name_with_dtype().items():
            if col_name in selected_columns:
                self._col_sql_dtype_map[col_name] = Utils.NUMPY_DTYPE_SQL_MAP.get(str(dtype),"VARCHAR(255)")
        self.dateTimeFormat()

    def setCase(self,case:str):
        self._selected_case = case.upper()

    def dateTimeFormat(self):
        exact_matches = ["date", "dt", "timestamp"]
        partial_matches = ["_date_", "_date", "_time_", "_dt_", "_dt", "_ts_", "_datetime_", "_date_time_"]

        date_pattern = re.compile(r"|".join(map(re.escape, [
            p for p in partial_matches if "date" in p or "dt" in p
        ])), flags=re.IGNORECASE)

        timestamp_pattern = re.compile(r"|".join(map(re.escape, [
            p for p in partial_matches if "timestamp" in p or "ts" in p
        ])), flags=re.IGNORECASE)

        for col in self._selected_columns:
            col_lower = str(col).lower().strip()

            if col_lower in exact_matches:
                if "date" in col_lower or "dt" in col_lower:
                    self._col_sql_dtype_map[col] = "DATE"
                else:
                    self._col_sql_dtype_map[col] = "TIMESTAMP"

            elif date_pattern.search(col_lower):
                self._col_sql_dtype_map[col] = "DATE"

            elif timestamp_pattern.search(col_lower):
                self._col_sql_dtype_map[col] = "TIMESTAMP"


    def _ddlDtypeChangeDasedOnDB(self,ddl:str)->str:
        db = self._db
        sql_data_types = Utils.SQL_TYPE_MAP
        generic_dtypes = list(set([dtype.upper() for dtype in Utils.NUMPY_DTYPE_SQL_MAP.values()]))

        for generic_type in generic_dtypes:
            generic_type = generic_type.split("(")[0] if "NUMBER" not in generic_type.split("(")[0] else generic_type
            if generic_type not in ddl.upper() or  generic_type not in sql_data_types.keys():
                continue

            ddl = ddl.replace(generic_type,sql_data_types.get(generic_type,dict()).get(db.upper(), 'VARCHAR2(255)'))

        return ddl



    def createDDL(self):
        to_case = Utils.changeCase(case=self._selected_case)
        column_list = ",\n \t".join([to_case(str(col_name))+"\t"+str(self._col_sql_dtype_map.get(col_name)) for col_name in self._selected_columns]).replace(" ","")

        if len(column_list) == 0 or column_list == None:
            return "# No columns found "

        ddl = "CREATE TABLE IF NOT EXISTS " + to_case(self._table_name) + " (\n \t"+column_list+"\n);"
        ddl = self._ddlDtypeChangeDasedOnDB(ddl)

        return ddl



    def createDML(self) -> str:
        to_case = Utils.changeCase(case=self._selected_case)
        dml_column_list_str = ",\n\t".join([to_case(str(col_name))  for col_name in self._selected_columns]).replace(" ", "")
        if len(dml_column_list_str) == 0 or dml_column_list_str == None:
            return "# No columns found "

        updated_data_set = self._dfh.get_df(self._selected_columns)
        last_row_count = int(self._dfh.get_shape()[0])

        for col,dataType in self._col_sql_dtype_map.items():

            if dataType.lower().find("number(38,0)") != -1:
                updated_data_set[col] = updated_data_set[col].astype(int)
            elif dataType.lower().find("number(38,2") != -1:
                updated_data_set[col] = updated_data_set[col].astype(float)
            elif dataType.lower().find('bool') != -1:
                updated_data_set[col] = updated_data_set[col].astype(str).str.upper()
            elif dataType.lower().find("date") != -1:
                updated_data_set[col] = "TO_DATE('"+updated_data_set[col].astype(str)+"','YYYY-MM-DD')"
            elif dataType.lower().find("timestamp") != -1:
                updated_data_set[col] = "'"+updated_data_set[col].astype(str)+"'"
            else:
                updated_data_set[col] = "'" +updated_data_set[col].astype(str)+ "'"
            # fill NULL
            updated_data_set[col] = updated_data_set[col].apply(lambda data: "NULL" if  any(sub in str(data).lower() for sub in  ["None","nan","NaN","NaT","''"]) else data)

        values = []
        for idx,row in enumerate(updated_data_set.itertuples(index = False)):
            val = ""
            if idx == 0 or idx%500 == 0:
                val = val+f"INSERT INTO {self._table_name} (\n\t{dml_column_list_str} \t\n)\nVALUES\n"
            val = val+("("+",".join([str(value) for value in row])+")"+(";\n" if idx+1 == last_row_count or (idx>0 and (idx+1)%500 == 0) else ",\n"))
            values.append(val)
        dml = "".join(values)
        # dml = f"INSERT INTO {self._table_name} (\n\t{dml_column_list_str} \t\n)\nVALUES\n{values}"

        return dml

