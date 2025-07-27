
import pandas as pd

class DFHandler:
    _df = None
    def __init__(self, df:pd.DataFrame = None):

        if df is None or df.shape[0] == 0:
            raise ValueError("Dataframe is empty or no dataframe provided")
        self._df = df


    def get_df(self,col_list:list = []):
        if len(col_list) > 0 and col_list is not None:
            return self._df[col_list]
        return self._df

    def get_column_names(self)->list:
        return self._df.columns.tolist()

    def get_shape(self):
        return self._df.shape

    def get_column_name_with_dtype(self) -> dict:
        return self._df.dtypes.to_dict()

    def fill_na(self, column_name: str = None, value=None):
        if column_name is not None and value is not None:
            self._df[column_name] = self._df[column_name].fillna(value)
        else:
            columns_with_dtype = self._df.dtypes.to_dict()
            for col in self.get_column_names():
                dtype = str(columns_with_dtype[col])
                if dtype == 'object':
                    self._df[col] = self._df[col].fillna('')
                elif dtype == 'int64':
                    self._df[col] = self._df[col].fillna(0)
                elif dtype == 'float64':
                    self._df[col] = self._df[col].fillna(0.0)

    def format_date(self, col_name):
        format_str = self._df[col_name].tolist()
        date_format = format_str.get('format')
        try:
            self._df[col_name] = (pd.to_datetime(self._df[col_name], format=date_format, errors='raise'))
            self._df[col_name] = self._df[col_name].dt.strftime("%Y-%m-%d")
        except ValueError as e:
            print(f"❌ Unable to parse date with format '{date_format}' in column '{col_name}': {e}")
            raise
        except Exception as e:
            raise ValueError(f"⚠️ Unexpected error while formatting date in column '{col_name}': {e}")

    def format_time(self, col_name):
        format_str = self._df[col_name].tolist()
        date_format = format_str.get('format')

    def format_timestamp(self, col_name):
        format_str = self._df[col_name].tolist()
        date_format = format_str.get('format')

        try:
            self._df[col_name] = pd.to_datetime(self._df[col_name], errors='raise')
            self._df[col_name] = self._df[col_name].dt.strftime('%Y-%m-%d %H:%M:%S')
        except ValueError as e:
            print(f"❌ Unable to parse timestamp in column '{col_name}': {e}")
            raise
        except Exception as e:
            raise ValueError(f"⚠️ Unexpected error while formatting timestamp in column '{col_name}': {e}")












