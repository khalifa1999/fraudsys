# import pandas as pd
# import streamlit as st
#
#
#
# st.title("Automation Application")
# st.subheader("IT traitement")
#
# uploaded_f = st.file_uploader('Choissez un fichier', type=['xlsx', 'xlsb'])
#
#
#
# # For IT
# def it():
#     # color function
#     def colour(value):
#         if value > 80:
#             color = 'red'
#         else:
#             color = 'green'
#         return 'color: %s' % color
#
#     it_df = pd.read_excel(uploaded_f, engine='openpyxl')
#     it_df = it_df.groupby('num_ligne')[['nb_appels']].sum()
#     it_df['outils'] = 'IT'
#     it_df = it_df.sort_values(
#         by='nb_appels',
#         ascending=False
#     )
#     it_df = it_df.style.applymap(colour, subset=['nb_appels'])
#     return it_df
#
#
# if uploaded_f is not None:
#     it_dataframe = it()
#     st.dataframe(it_dataframe)
#
#     # for it
#     unique_val = len(it_dataframe.index.unique())
#     st.write(unique_val)
#
