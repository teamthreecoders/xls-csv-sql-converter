import re
import scripts.file_handler as fh
import scripts.df_handler as dfh
import streamlit as st
from utils.utils import Utils

import scripts.export_file_handler as efh

def page1():
    # new instance
    file_handler = fh.Filehandler()
    # get upload file path
    UPLOAD_FILE_PATH = file_handler.loadFile()
    # check file path have contained or not

    if UPLOAD_FILE_PATH is None:
        st.error("Upload File (.xls, .csv)")
        return

    st.success("Uploaded file:: \t"+ UPLOAD_FILE_PATH.name)

    if UPLOAD_FILE_PATH.name.endswith(".xls"):
        df = file_handler.readExcel()
    elif UPLOAD_FILE_PATH.name.endswith(".csv"):
        df = file_handler.readCsv()

    else:
        st.error("File type not supported")
        return

    # Load data to pandas df
    try:
        DF_HANDLER = dfh.DFHandler(df)
    except ValueError:
        st.error("Can not load the file")
        return



    row_cnt_container,col_cnt_container = st.columns([0.5,0.5])
    row_cnt,col_cnt = DF_HANDLER.get_shape()
    with row_cnt_container:
        st.markdown(f"<h4>Total rows: {row_cnt}</h4>", unsafe_allow_html=True)
    with col_cnt_container:
        st.markdown(f"<h4>Total columns: {col_cnt}</h4>", unsafe_allow_html=True)


    st.title("Sample data")
    st.markdown("---")
    df_col_list = DF_HANDLER.get_column_names()

    selected_columns = st.multiselect("Choose columns:", options=df_col_list, default=df_col_list)
    # show dataframe
    DF_CONTENT = DF_HANDLER.get_df(col_list=selected_columns)

    st.dataframe(DF_CONTENT.head(10))

    # # ask for fill NA value
    # st.text("Fill null value")
    # col1,col2 = st.columns(2,border=False,gap="medium")
    # with col1:
    #     st.text("Column:")
    #     for col in df_col_list:
    #         st.write(col)
    #         st.write("Count NA :"+ DF_CONTENT[col].isnull().sum().__str__())
    #
    #
    # with col2:
    #     st.text("Fill value:")
    #     i = 0
    #     for col, dtype in DF_HANDLER.get_column_name_with_dtype().items():
    #         user_input = st.text_input(col, key=col+str(i))
    #
    #         if user_input.strip() != "":
    #             try:
    #                 # A mapping from numpy dtype to actual callable Python conversion functions
    #                 dtype_map = {
    #                     'int64': int,
    #                     'float64': float,
    #                     'bool': lambda x: x.lower() in ['true', '1', 'yes'],
    #                     'object': str,
    #                     # Add more mappings if needed
    #                 }
    #
    #                 # Assuming `dtype` is a numpy.dtype object
    #                 actual_type = dtype.name  # e.g., 'int64', 'float64', etc.
    #
    #                 convert_func = dtype_map.get(actual_type, str)  # default to str if unknown
    #
    #                 # Convert to correct type
    #                 value = convert_func(user_input.strip())
    #
    #                 # Create a unique key for each button
    #                 update_key = f"update_{col}".upper()
    #
    #                 st.button(
    #                     f"update_{col}".upper(),
    #                     key=update_key,
    #                     on_click=partial(DF_HANDLER.fill_na, col, value)
    #                 )
    #                 i = i+1
    #             except ValueError:
    #                 st.error(f"Invalid value for column {col} with type {dtype.__name__}")


    st.title("DDL / DML Files:")
    st.markdown("---")
    table_name = st.text_input("Enter the table name:", max_chars=255, placeholder="Enter the table name:")

    def is_valid_table_name(name):
        return bool(re.match(r'^([A-Za-z_][A-Za-z0-9_]*)(\.[A-Za-z_][A-Za-z0-9_]*){0,2}$', name))

    # Show validation warning
    if table_name and not is_valid_table_name(table_name):
        st.error(
            "❌ Invalid table name. It must start with a letter or underscore and contain only letters, numbers, or underscores.")

    # Optional: stop further processing if invalid
    if not table_name:
        st.warning("⚠️ Please enter table name.")
        return

    elif not is_valid_table_name(table_name):
        st.stop()


    db_names = list(Utils.SQL_TYPE_MAP['VARCHAR2'].keys())  # ['ORACLE', 'MYSQL', 'POSTGRES', 'SNOWFLAKE', 'SINGLESTORE']

    # Create 3 radio buttons in a single row (you can show more if needed)


    selected_db = st.radio("Select database:", options=db_names, key="select_db")

    try:
        export = efh.ExportFileHandler(df,selected_columns,table_name,selected_db)
    except ValueError as e:
        print(e)
        st.error("Something went wrong..." )
        st.error(e)
        return

    except Exception as e:
        print("ERROR" )
        print(e)
        return



    with st.spinner("Preparing SQL scripts...",_cache=False):
        ddl_sql = export.createDDL()
        dml_sql = export.createDML()
        st.success("✅ SQL generation complete!")

        # DDL Section
    ddl_col1, ddl_col2 = st.columns([4, 2])
    with ddl_col1:
        st.markdown("<h3>DDL file</h3>",unsafe_allow_html=True)
    with ddl_col2:
        st.download_button(
            "Download DDL",
            icon=":material/download:",
            data=ddl_sql,
            file_name=f"{table_name}_ddl.sql",
            mime="text/sql",
            help="Click me to download the DDL script"
        )
    if col_cnt > 5000:
        st.warning("😢DDL file is too large to display in the page. Please download it.")
    else:
        st.code(ddl_sql, language="sql", height=300)

    # DML Section
    dml_col1, dml_col2 = st.columns([4, 2])
    with dml_col1:
        st.markdown("<h3>DML file</h3>",unsafe_allow_html=True)
    with dml_col2:
        st.download_button(
            "Download DML",
            icon=":material/download:",
            data=dml_sql,
            file_name=f"{table_name}_dml.sql",
            mime="text/sql",
            help="Click me to download the DML script"
        )
    if row_cnt > 5000:
        st.warning("😢DML file is too large to display in the page. Please download it.")
    else:
        st.code(dml_sql, language="sql", height=400)




























