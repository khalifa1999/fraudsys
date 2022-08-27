import streamlit as st
import pandas as pd
from todict import pays

st.title("Automation Application")
st.subheader("Radar traitement")

uploaded_f = st.sidebar.file_uploader("Choose xlsx file", type=['xlsx', 'xlsb'])


# For radar
@st.experimental_memo
def radar():
    df = pd.read_excel(uploaded_f, engine='openpyxl')
    df["Valeur d'aggregation"] = pd.to_numeric(df["Valeur d'aggregation"])


    return df


if uploaded_f is not None:
    hvi_dataframe = radar()
    st.dataframe(hvi_dataframe)

    # for radar
    unique_val = len(hvi_dataframe.index.unique())
    st.write(unique_val)

    # Use dataframe to make our treatments
    cdr = hvi_dataframe[["Valeur d'aggregation", "Nombre de cdr participants", "Pays Origine"]]
    cdr = cdr.sort_values(
        "Nombre de cdr participants",
        ascending=False
    )


    # color function
    def colour(value):
        if value > 80:
            color = 'red'
        else:
            color = 'green'
        return 'color: %s' % color


    cdr = cdr.style.applymap(colour, subset=["Nombre de cdr participants"])
    st.dataframe(cdr)

    st.write(pays.keys())

    # Valeur d'aggregation splitter values
    id = hvi_dataframe["Valeur d'aggregation"].to_dict()
    idval = id.values()
    import math
