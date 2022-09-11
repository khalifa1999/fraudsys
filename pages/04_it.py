import base64
from io import BytesIO  # Standard Python Module

import pandas as pd
import phonenumbers
import streamlit as st
from phonenumbers import geocoder

from filter import filter_dataframe

st.title("Automation Application")
st.subheader("IT traitement")

uploaded_f = st.sidebar.file_uploader("Choose xlsx file", type=['xlsx', 'xlsb'], key='itFile')
# Supprimer les valeurs uniques pour IT
# Faire des traitements complementqires et s'assurer que tout concorde

# For IT
def generate_excel_download_link(df):
    # Credit Excel: https://discuss.streamlit.io/t/how-to-add-a-download-excel-csv-function-to-a-button/4474/5
    towrite = BytesIO()
    df.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">Download Excel File</a>'
    return st.markdown(href, unsafe_allow_html=True)


def it():
    # color function
    def colour(value):
        if value >= 80:
            color = 'red'
        else:
            color = 'green'
        return 'color: %s' % color

    df = pd.read_excel(uploaded_f, engine='openpyxl')

    df['Indicatif'] = df["num_ligne"].astype(str).str.replace('.', '').str[0:3]
    df['cleanumber'] = df["num_ligne"].astype(str).str.replace('\.0', '')

    # st.write(type("+34636991906"))
    # st.write("+34636991906")

    df['retransformation'] = df['cleanumber'].apply(lambda x: "+" + str(x))
    parse = phonenumbers.parse(df['retransformation'][1])
    # st.write(geocoder.description_for_number(parse, 'en'))

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

    it_df = df.groupby(['num_ligne', 'pays'], as_index=False)[['nb_appels']].sum()

    it_df['outils'] = "IT"

    biggest = len(it_df.index.unique().tolist())
    # slider = st.sidebar.slider(
    #    "We're gonna display the different functions depending of the slide value", 1, biggest, 10
    # )
    # it_df = it_df.nlargest(slider, 'nb_appels')

    it_df = it_df.sort_values(
        by='nb_appels',
        ascending=False
    )
    it_df = it_df.style.applymap(colour, subset=['nb_appels'])
    return it_df


if uploaded_f is not None:
    it_dataframe = it()

    unique_val = len(it_dataframe.index.unique())
    st.write(unique_val)
    st.dataframe(filter_dataframe(it_dataframe))

    generate_excel_download_link(it_dataframe)

    # for it
