import base64
from io import BytesIO  # Standard Python Module

import pandas as pd
import streamlit as st
from filter import filter_dataframe


st.title("Automation Application")
st.subheader("HVI traitement")
uploaded_fhvi = st.sidebar.file_uploader('Choissez un fichier', type=['xlsx', 'xlsb'],  key='hviFile')



def generate_excel_download_link(df):
    # Credit Excel: https://discuss.streamlit.io/t/how-to-add-a-download-excel-csv-function-to-a-button/4474/5
    towrite = BytesIO()
    df.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">Download Excel File</a>'
    return st.markdown(href, unsafe_allow_html=True)


@st.experimental_memo
def hvi():
    hvi_df = pd.read_excel(uploaded_fhvi, engine='openpyxl')
    hvi_df['h_appel'] = pd.to_datetime(hvi_df['h_appel'])

    # st.write([type(k) for k in pays.keys()])
    # for keys, value in pays.items():
    #     if keys in df['first_range']:
    #         df['checked'] = "True"
    #
    #         df['checked'] = "False"
    return hvi_df


if uploaded_fhvi is not None:
    hvi_dataframe = hvi()
    hvi_dataframe = hvi_dataframe.sort_values('h_appel', ascending=True)
    st.dataframe(filter_dataframe(hvi_dataframe))

    # for hvi
    unique_val = len(hvi_dataframe['h_appel'].unique())

    st.write("nombre de numéros uniques ")
    st.write(unique_val)
    # st.write(hvi_dataframe)
    generate_excel_download_link(hvi_dataframe)

    # Download function
