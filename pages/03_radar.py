import base64
from io import BytesIO  # Standard Python Module

import pandas as pd
import streamlit as st

from filter import filter_dataframe

st.title("Automation Application")
st.subheader("Radar traitement")

uploaded_fradar = st.sidebar.file_uploader('Choose xlsx file', type=['xlsx', 'xlsb'], key='radarFile')


def generate_excel_download_link(df):
    # Credit Excel: https://discuss.streamlit.io/t/how-to-add-a-download-excel-csv-function-to-a-button/4474/5
    towrite = BytesIO()
    df.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">Download Excel File</a>'
    return st.markdown(href, unsafe_allow_html=True)


# For radar
@st.experimental_singleton
def radar():
    df = pd.read_excel(uploaded_fradar, engine='openpyxl')
    df["Valeur d'aggregation"] = pd.to_numeric(df["Valeur d'aggregation"])
    df['range 8'] = df["Valeur d'aggregation"].astype(str).str.replace('.', '').str[0:8]
    df['Outils'] = "Radar"
    df['Date de creation'] = df['Date de creation']

    # creer une colonne range verifier si un range y apparait plus de 2 fois grace
    # a count restituer cela sous forme de df avec le range et le compte
    return df


if uploaded_fradar is not None:
    radar_dataframe = radar()

    # for radar

    # Use dataframe to make our treatments
    cdr = radar_dataframe.groupby(["Valeur d'aggregation", "Outils", "Date de creation", "Pays Origine", "range 8"],
                                  as_index=False)[
        ['Nombre de cdr participants']].sum()
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




    # Color of the range





    # Let's apply the sorting function
    unique_val = len(cdr["Valeur d'aggregation"].unique())
    st.write(unique_val)
    cdr = cdr.drop_duplicates(subset="Valeur d'aggregation", keep='first')


    range_display = cdr['range 8'].value_counts(dropna=False)

    biggest = len(radar_dataframe["Valeur d'aggregation"].unique().tolist())
    slider = st.sidebar.slider(
        "We're gonna display the different functions depending of the slide value", 1, biggest, 30
    )
    cdr = cdr.nlargest(slider, 'Nombre de cdr participants')

    cdr = cdr.style.applymap(colour, subset=["Nombre de cdr participants"])
    # cdr = cdr.style.applymap(range_id, subset=["range 8"])

    # cpt = 0
    # for x in range_display.index:
            # st.write(range_display.index)
            # cpt += 1


    def range_id(value):
        if pd.value_counts(value) > 0:
            color = 'orange'
        else:
            color = 'green'

        return 'color: %s' % color


    # st.dataframe(cdr)

    st.dataframe(filter_dataframe(cdr))
    st.dataframe(range_display)

    if st.button('Clear All'):
        st.experimental_singleton.clear()





    # st.write(pays.keys())

    # Valeur d'aggregation splitter values
    # id = radar_dataframe["Valeur d'aggregation"].to_dict()
    # idval = id.values()
