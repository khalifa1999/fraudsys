import pandas as pd
import phonenumbers
import streamlit as st
from phonenumbers import geocoder

uploaded_ibasis = st.sidebar.file_uploader("Choose a excel file", type=['xlsx', 'xlsb'], key='ibasisFile')


def ibasis():
    ibasis_df = pd.read_excel(uploaded_ibasis, engine='openpyxl')
    unique = len(ibasis_df['B Num'].unique())

    ibasis_df['B Num'] = ibasis_df['B Num'].apply(lambda x: "+" + str(x))

    # st.write(geocoder.description_for_number(parse, 'en'))

    ibasis_df['Pays'] = ""

    cpt = 0
    for x in ibasis_df['B Num']:
        try:
            parse = phonenumbers.parse(ibasis_df['B Num'][cpt])
            pays = geocoder.description_for_number(parse, 'en')
            # st.write(pays)
            ibasis_df['Pays'][cpt] = pays
        except ValueError as e:
            raise Exception('Erreur sur le numero from ') from e
            pass
        cpt += 1

    df = ibasis_df.groupby(['B Num', 'Pays'], as_index=False).nunique()
    new = df[['B Num', 'Pays']]
    st.write(unique)
    return new


if uploaded_ibasis is not None:
    display = ibasis()
    st.dataframe(display)
