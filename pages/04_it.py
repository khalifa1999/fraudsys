import streamlit as st
import pandas as pd

st.title("Automation Application")
st.subheader("IT traitement")


uploaded_f = st.sidebar.file_uploader("Choose xlsx file", type=['xlsx', 'xlsb'], key='itFile')


# For IT

def it():
    # color function
    def colour(value):
        if value > 80:
            color = 'red'
        else:
            color = 'green'
        return 'color: %s' % color

    df = pd.read_excel(uploaded_f, engine='openpyxl')

    it_df = df.groupby('num_ligne')[['nb_appels', 'heure']].sum()
    it_df['outils'] = "IT"
    it_df = it_df.sort_values(
        by='nb_appels',
        ascending=False
    )
    it_df = it_df.style.applymap(colour, subset=['nb_appels'])
    return it_df


if uploaded_f is not None:
    it_dataframe = it()
    st.dataframe(it_dataframe)

    # for it
    unique_val = len(it_dataframe.index.unique())
    st.write(unique_val)