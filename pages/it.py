import streamlit as st
import pandas as pd

st.title("Automation Application")
st.subheader("IT traitement")


uploaded_f = st.sidebar.file_uploader("Choose xlsx file", type=['xlsx', 'xlsb'])


# For IT
@st.experimental_memo
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
    hvi_dataframe = it()
    st.dataframe(hvi_dataframe)

    # for it
    unique_val = len(hvi_dataframe.index.unique())
    st.write(unique_val)
