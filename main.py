import streamlit as st
import pandas as pd
from phonenumbers import geocoder
import phonenumbers
st.set_page_config(page_title="DFC APP",
                   page_icon=None, layout="centered", initial_sidebar_state="auto"
                   )

st.title("Automation Application")
st.subheader("Welcome to dfc fraud automation app")


uploaded_f = st.sidebar.file_uploader("Choose xlsx file", type=['xlsx', 'xlsb'], key='temp')


@st.experimental_memo
def temp():
    df = pd.read_excel(uploaded_f, engine='openpyxl')

    df['cleanumber'] = df["Numero"].astype(str).str.replace('\.0', '')

    # st.write(type("+34636991906"))
    # st.write("+34636991906")

    df['retransformation'] = df['cleanumber'].apply(lambda x: "+" + str(x))


    list = df['retransformation'].values.tolist()
    st.write(list)
    df['pays'] = ""

    cpt = 0
    for x in df['retransformation']:
        try:
            parse = phonenumbers.parse(df['retransformation'][cpt])
            pays = geocoder.description_for_number(parse, 'en')
            # st.write(pays)
            df['pays'][cpt] = pays
        except ValueError as e:
            raise Exception('Erreur sur le numero from ') from e
            pass
        cpt += 1
    return df


if uploaded_f is not None:
    it_dataframe = temp()
    st.dataframe(it_dataframe)
