import streamlit as st
import pandas as pd
from todict import pays
from todict import generate_excel_download_link

st.title("Automation Application")
st.subheader("HVI traitement")

uploaded_f = st.sidebar.file_uploader("Choose xlsx file", type=['xlsx', 'xlsb'])


# For hvi
@st.experimental_memo
def hvi():
    df = pd.read_excel(uploaded_f, engine='openpyxl')
    df['num_ligne'] = df['num_ligne']
    df['h_appel'] = pd.to_datetime(df['h_appel'])

    df['first_range'] = df['num_ligne'].astype(str).str.replace('.', '').str[0:3]
    df['first_range'] = df['first_range'].astype(int)
    st.write(df['first_range'].dtype)
    st.write([type(k) for k in pays.keys()])
    for keys, value in pays.items():
        if keys in df['first_range']:
            df['checked'] = "True"
        else:
            df['checked'] = "False"

    df = df.sort_values('h_appel', ascending=True)
    dataframe = df[['num_ligne', 'h_appel']]
    return dataframe


if uploaded_f is not None:
    hvi_dataframe = hvi()
    st.dataframe(hvi_dataframe)
    # for hvi
    unique_val = len(hvi_dataframe['h_appel'].unique())

    st.write("nombre de numéros uniques ")
    st.write(unique_val)
    # st.write(hvi_dataframe)

    # Download function

    generate_excel_download_link(hvi_dataframe)
