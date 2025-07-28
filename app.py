# package

import streamlit as st
import webPages.page1 as page1


def app():
    # st.sidebar()

    st.set_page_config(
        page_title="XLS and CSV to SQL Converter",
        page_icon="media/5e0706fd002e536e.png",  # Or use a path to a custom .ico/.png
        layout="centered",  # Or "wide"

    )

    st.markdown("""
        <h2 style='text-align: left;'>
            📄 XLS and CSV to DDL and DML Converter
        </h2>
        <hr/>
    """, unsafe_allow_html=True)
    page1.page1()
    st.markdown("---")
    st.markdown("**© Developed with ❤️ by Ayan**", help="Author info")


if __name__ == '__main__':
    app()