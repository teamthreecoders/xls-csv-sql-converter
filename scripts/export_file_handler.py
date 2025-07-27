import re
import pandas as pd
import scripts.df_handler as dfh
from utils.utils import Utils

class ExportFileHandler:
    def __init__(self, dataframe:pd.DataFrame = None ,selected_columns:list = [], table_name:str = "",db_name:str="SNOWFLAKE"):
        if dataframe is None or dataframe.shape[0] == 0:
            raise ValueError("Dataframe is empty")
        if len(selected_columns) == 0:
            raise ValueError("Selected columns are empty")
        if table_name == "":
            raise ValueError("Table name could not be empty")

        self._dfh = dfh.DFHandler(dataframe)
        self._selected_columns = selected_columns
        self._table_name = table_name
        self._db = db_name
        self._col_mapping = dict()

        for col_name,dtype in self._dfh.get_column_name_with_dtype().items():
            if col_name in self._selected_columns:
                self._col_mapping[col_name] = Utils.NUMPY_DTYPE_SQL_MAP.get(str(dtype),"VARCHAR(255)")


        self.dateTimeFormat()

    def dateTimeFormat(self):
        exact_matches = ["date", "dt", "timestamp"]
        partial_matches = ["_date_", "_date", "_time_", "_dt_", "_dt", "_ts_", "_datetime_", "_date_time_"]

        date_pattern = re.compile(r"|".join(map(re.escape, [
            p for p in partial_matches if "date" in p or "dt" in p
        ])), flags=re.IGNORECASE)

        timestamp_pattern = re.compile(r"|".join(map(re.escape, [
            p for p in partial_matches if "timestamp" in p or "ts" in p
        ])), flags=re.IGNORECASE)

        for col in self._col_mapping.keys():
            col_lower = str(col).lower().strip()

            if col_lower in exact_matches:
                if "date" in col_lower or "dt" in col_lower:
                    self._col_mapping[col] = "DATE"
                else:
                    self._col_mapping[col] = "TIMESTAMP"

            elif date_pattern.search(col_lower):
                self._col_mapping[col] = "DATE"

            elif timestamp_pattern.search(col_lower):
                self._col_mapping[col] = "TIMESTAMP"


    def _ddlDtypeChangeDasedOnDB(self,ddl:str)->str:
        db = self._db
        sql_data_types = Utils.SQL_TYPE_MAP
        generic_dtypes = list(set([dtype.upper() for dtype in Utils.NUMPY_DTYPE_SQL_MAP.values()]))

        for generic_type in generic_dtypes:
            generic_type = generic_type.split("(")[0]
            if generic_type not in ddl.upper() or  generic_type not in sql_data_types.keys():
                continue

            ddl = ddl.replace(generic_type,sql_data_types.get(generic_type,dict()).get(db.upper(), 'VARCHAR2(255)'))

        return ddl


    def createDDL(self):
        column_list = ",\n \t".join([str(col_name)+"\t"+str(self._col_mapping.get(col_name)) for col_name in self._selected_columns]).replace(" ","")
        if len(column_list) == 0 or column_list == None:
            return "# No columns found "

        ddl = "CREATE TABLE IF NOT EXISTS " + self._table_name + " (\n \t"+column_list+"\n);"
        ddl = self._ddlDtypeChangeDasedOnDB(ddl)

        return ddl

    def createDML(self) -> str:
        dml_column_list_str = ",\n\t".join([str(col_name)  for col_name in self._selected_columns]).replace(" ", "")
        if len(dml_column_list_str) == 0 or dml_column_list_str == None:
            return "# No columns found "

        updated_data_set = self._dfh.get_df(self._selected_columns)

        for col,value in self._col_mapping.items():
            if value.lower().find("int") != -1:
                updated_data_set[col] = updated_data_set[col].astype(int)
            elif value.lower().find("float") != -1:
                updated_data_set[col] = updated_data_set[col].astype(float)
            elif value.lower().find('bool') != -1:
                updated_data_set[col] = updated_data_set[col].astype(str).str.upper()
            elif value.lower().find("date") != -1:
                updated_data_set[col] = "TO_DATE('"+updated_data_set[col].astype(str)+"','YYYY-MM-DD')"
            elif value.lower().find("timestamp") != -1:
                updated_data_set[col] = "TO_TIMESTAMP_NTZ('"+updated_data_set[col].astype(str)+"','YYYY-MM-DD HH24:MI:SS')"
            else:
                updated_data_set[col] = "'" +updated_data_set[col].astype(str)+ "'"

        last_row_count = int(self._dfh.get_shape()[0])

        values = []
        for idx,row in enumerate(updated_data_set.itertuples(index = False)):
            val = ("("+",".join([str(value) for value in row])+")"+(";\n" if idx+1 == last_row_count else ",\n"))
            val = val.replace("'None'","NULL")
            val = val.replace("'nan'","NULL")
            val = val.replace("'NaN'","NULL")
            val = val.replace("'NaT'","NULL")
            val = val.replace("''","NULL")
            values.append(val)
        values = "".join(values)
        dml = f"INSERT INTO {self._table_name} (\n\t{dml_column_list_str} \t\n)\nVALUES\n{values}"

        return dml


