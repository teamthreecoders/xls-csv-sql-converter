
import streamlit as st
import pandas as pd


class Filehandler:

    _filePath = None

    def __init__(self):
        pass

    def loadFile(self) :
        self._filePath = st.file_uploader("Upload file", type=["csv","xls","xlsx"])

        if self._filePath is not None :
             return self._filePath
        else:
            return None

    def downLoadButton(self, file_content = None, btn_title:str = "",file_name:str = None)->None:
        if file_content is not None and file_content != "" and btn_title is not None and btn_title != "" and file_name is not None and file_name != None:
            st.download_button(btn_title, file_content, file_name=file_name)
        else:
            st.error("Please provide all the required parameters")

    def readExcel(self):
        if self._filePath is not None:
            if self._filePath.name.endswith(".xls") or self._filePath.name.endswith(".xlsx"):
                return pd.read_excel(self._filePath)
            else:
                st.error("Please upload a valid excel file")
        else:
            st.error("Please upload a file")
        return None

    def readCsv(self):
        if self._filePath is not None:

            if self._filePath.name.endswith(".csv"):
                return pd.read_csv(filepath_or_buffer=self._filePath)
            else:
                st.error("Please upload a valid csv file")
        else:
            st.error("Please upload a file")
        return None

