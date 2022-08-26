import streamlit as st
import pandas as pd

st.title("Automation Application")
st.subheader("HVI traitement")

uploaded_f = st.sidebar.file_uploader("Choose xlsx file", type=['xlsx', 'xlsb'])


# For hvi
@st.experimental_memo
def hvi():
    df = pd.read_excel(uploaded_f, engine='openpyxl')
    df['num_ligne'] = df['num_ligne']
    df['h_appel'] = pd.to_datetime(df['h_appel'])
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
