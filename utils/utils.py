
class Utils:
    NUMPY_DTYPE_SQL_MAP = {
        # based on snpwflake
        'int8': 'NUMBER(38,0)',
        'int16': 'NUMBER(38,0)',
        'int32': 'NUMBER(38,0)',
        'int64': 'NUMBER(38,0)',
        'uint8': 'NUMBER(38,0)',
        'uint16': 'NUMBER(38,0)',
        'uint32': 'NUMBER(38,0)',
        'uint64': 'NUMBER(38,0)',
        'float16': 'NUMBER(38,2)',
        'float32': 'NUMBER(38,2)',
        'float64': 'NUMBER(38,2)',
        'bool': 'BOOLEAN',
        'bool_': 'BOOLEAN',
        'object': 'VARCHAR2(50)',
        'str': 'VARCHAR2(50)',
        'str_': 'VARCHAR2(50)',
        'string_': 'VARCHAR2(225)',
        'datetime64[ns]': 'TIMESTAMP_NTZ',
        'datetime64[D]': 'DATE',
        'timedelta64[ns]': 'INTERVAL',
        'category': 'VARCHAR2(50)',
        'complex64': 'VARCHAR2(50)',  # Could also be rejected if unsupported
        'complex128': 'VARCHAR2(50)'  # Could also be rejected if unsupported

    }

    SQL_TYPE_MAP = {
        'VARCHAR2': {
            'ORACLE': 'VARCHAR2',
            'MYSQL': 'VARCHAR',
            'POSTGRES': 'VARCHAR',
            'SNOWFLAKE': 'VARCHAR2',
            'SINGLESTORE': 'VARCHAR'
        },
        'TEXT': {
            'ORACLE': 'CLOB',
            'MYSQL': 'TEXT',
            'POSTGRES': 'TEXT',
            'SNOWFLAKE': 'TEXT',
            'SINGLESTORE': 'TEXT'
        },
        'INTEGER': {
            'ORACLE': 'NUMBER',
            'MYSQL': 'INT',
            'POSTGRES': 'INTEGER',
            'SNOWFLAKE': 'INTEGER',
            'SINGLESTORE': 'INT'
        },
        'NUMBER(38,0)': {
            'ORACLE': 'NUMBER(38,0)',
            'MYSQL': 'BIGINT(20)',
            'POSTGRES': 'BIGINT',
            'SNOWFLAKE': 'NUMBER(38,0)',
            'SINGLESTORE': 'BIGINT(20)'
        },
        'NUMBER(38,2)': {
            'ORACLE': 'NUMBER(38,2)',
            'MYSQL': 'DECIMAL(38,2)',
            'POSTGRES': 'REAL',
            'SNOWFLAKE': 'NUMBER(38,2)',
            'SINGLESTORE': 'DECIMAL(38,2)'
        },
        'DOUBLE': {
            'ORACLE': 'BINARY_DOUBLE',
            'MYSQL': 'DOUBLE',
            'POSTGRES': 'DOUBLE PRECISION',
            'SNOWFLAKE': 'DECIMAL(38,2)',
            'SINGLESTORE': 'DOUBLE'
        },
        'DECIMAL': {
            'ORACLE': 'NUMBER',
            'MYSQL': 'NUMBER(38,2)',
            'POSTGRES': 'NUMERIC',
            'SNOWFLAKE': 'NUMBER(38,2)',
            'SINGLESTORE': 'DECIMAL(38,2)'
        },
        'BOOLEAN': {
            'ORACLE': 'NUMBER(1)',
            'MYSQL': 'BOOLEAN',
            'POSTGRES': 'BOOLEAN',
            'SNOWFLAKE': 'BOOLEAN',
            'SINGLESTORE': 'TINYINT(1)'  # BOOLEAN is an alias for TINYINT(1)
        },
        'DATE': {
            'ORACLE': 'DATE',
            'MYSQL': 'DATE',
            'POSTGRES': 'DATE',
            'SNOWFLAKE': 'DATE',
            'SINGLESTORE': 'DATE'
        },
        'DATETIME': {
            'ORACLE': 'DATE',
            'MYSQL': 'DATETIME',
            'POSTGRES': 'TIMESTAMP',
            'SNOWFLAKE': 'TIMESTAMP_NTZ',
            'SINGLESTORE': 'DATETIME'
        },
        'TIMESTAMP': {
            'ORACLE': 'TIMESTAMP',
            'MYSQL': 'TIMESTAMP',
            'POSTGRES': 'TIMESTAMP',
            'SNOWFLAKE': 'TIMESTAMP_NTZ',
            'SINGLESTORE': 'TIMESTAMP'
        },
        'TIME': {
            'ORACLE': 'INTERVAL DAY TO SECOND',
            'MYSQL': 'TIME',
            'POSTGRES': 'TIME',
            'SNOWFLAKE': 'TIME',
            'SINGLESTORE': 'TIME'
        }
    }

    ORACLE_DATE_TYPE = {
        # Pure Date Formats
        'DD/MM/YYYY': '%d/%m/%Y',
        'YYYY-MM-DD': '%Y-%m-%d',
        'MM/DD/YYYY': '%m/%d/%Y',
        'DD-MON-YYYY': '%d-%b-%Y',  # Month as short name
        'DD-MON-RR': '%d-%b-%y',
        'YYYY/MM/DD': '%Y/%m/%d',

        # Timestamp Formats
        'YYYY-MM-DD HH24:MI:SS': '%Y-%m-%d %H:%i:%s',
        'DD/MM/YYYY HH24:MI:SS': '%d/%m/%Y %H:%i:%s',
        'MM/DD/YYYY HH24:MI:SS': '%m/%d/%Y %H:%i:%s',
        'YYYY/MM/DD HH24:MI:SS': '%Y/%m/%d %H:%i:%s',
        'DD-MON-YYYY HH24:MI:SS': '%d-%b-%Y %H:%i:%s',

        # With fractional seconds
        'YYYY-MM-DD HH24:MI:SS.FF': '%Y-%m-%d %H:%i:%s.%f',
        'DD/MM/YYYY HH24:MI:SS.FF': '%d/%m/%Y %H:%i:%s.%f',

        # 12-hour format (Oracle with AM/PM)
        'DD/MM/YYYY HH:MI:SS AM': '%d/%m/%Y %h:%i:%s %p',
        'YYYY-MM-DD HH:MI:SS PM': '%Y-%m-%d %h:%i:%s %p',

        # ISO-like formats
        'YYYY-MM-DD"T"HH24:MI:SS': '%Y-%m-%dT%H:%i:%s',

        # Year-Month formats
        'YYYY-MM': '%Y-%m',
        'MM-YYYY': '%m-%Y'
    }
    @classmethod
    def changeCase(cls,case:str="UPPER"):
        col_case = case.upper().replace("CASE", "")

        if col_case == "UPPER":
            to_case = lambda x: x.upper()
        elif col_case == "LOWER":
            to_case = lambda x: x.lower()
        elif col_case == "CAPITALIZE":
            to_case = lambda x: x.capitalize()
        elif col_case == "TITLE":
            to_case = lambda x: x.title()
        elif col_case == "SWAP":
            to_case = lambda x: x.swapcase()
        else:
            to_case = lambda x: x
        return to_case



