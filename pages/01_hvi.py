import streamlit as st
import pandas as pd
from io import StringIO, BytesIO  # Standard Python Module
import base64

st.title("Automation Application")
st.subheader("HVI traitement")

uploaded_f = st.sidebar.file_uploader("Choose xlsx file", type=['xlsx', 'xlsb'])


def generate_excel_download_link(df):
    # Credit Excel: https://discuss.streamlit.io/t/how-to-add-a-download-excel-csv-function-to-a-button/4474/5
    towrite = BytesIO()
    df.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">Download Excel File</a>'
    return st.markdown(href, unsafe_allow_html=True)

pays = {1: 'US/Canada', 1242: 'Bahamas', 1246: 'Barbade', 1264: 'Anguilla', 1268: 'Antigua et Barbuda',
        1284: 'Iles Vierges Britanniques', 1340: 'Iles Vierges Americaines', 1345: 'Iles Caïmans', 1441: 'Bermudes',
        1473: 'Grenade', 1649: 'Iles Turques-et-Caïques', 1664: 'Montserrat', 1670: 'Marianne du Nord', 1671: 'Guam',
        684: 'Iles Samoa Américaines', 1758: 'Sainte Lucie', 1767: 'Dominique', 1784: 'Saint-Vincent-et-les Grenadines',
        1787: 'Porto Rico', 18: 'République Dominicaine',
        1868: 'Trinité-et-Tobago', 1869: 'Saint-Christophe-et-Niévès', 1876: 'Jamaïque', 20: 'Egypte', 212: 'Maroc',
        213: 'Algérie', 216: 'Tunisie', 218: 'Libye', 220: 'Gambie', 221: 'Sénégal', 222: 'Mauritanie', 223: 'Mali',
        224: 'Guinée', 225: "Côte d'Ivoire", 226: 'Burkina Faso', 227: 'Niger', 228: 'Togo', 229: 'Bénin',
        230: 'Maurice', 231: 'Liberia', 232: 'Sierra-Leone', 233: 'Ghana', 234: 'Nigeria', 235: 'Tchad',
        236: 'République Centrafricaine', 237: 'Cameroun', 238: 'Cap Vert',
        240: 'Guinée Equatoriale', 241: 'Gabon', 242: 'Congo', 243: 'Rép. Dém. du Congo', 244: 'Angola',
        248: 'Seychelles', 249: 'Soudan', 250: 'Rwanda', 251: 'Ethiopie', 253: 'Djibouti', 254: 'Kenya',
        255: 'Tanzanie', 256: 'Ouganda', 257: 'Burundi', 258: 'Mozambique', 260: 'Zambie', 261: 'Madagascar',
        263: 'Zimbabwe', 264: 'Namibie', 265: 'Malawi', 266: 'Lesotho', 267: 'Botswana', 268: 'Swaziland',
        269: 'Comores', 27: 'République Sud-Africaine', 291: 'Erythrée', 297: 'Aruba', 211: 'Soudan du Sud',
        298: 'Iles Faroes', 245: 'Guinée-Bissau', 30: 'Grèce', 31: 'Pays-Bas', 32: 'Belgique', 33: 'France',
        34: 'Espagne', 34928: 'Iles Canaries', 350: 'Gibraltar', 351: 'Portugal', 352: 'Luxembourg', 353: 'Irlande',
        354: 'Islande', 355: 'Albanie', 356: 'Malte', 357: 'Chypre Sud', 358: 'Finlande', 359: 'Bulgarie',
        36: 'Hongrie', 370: 'Lituanie', 371: 'Lettonie', 372: 'Estonie', 373: 'Moldavie', 374: 'Arménie',
        375: 'Biélorussie', 376: 'Andorre', 377: 'Monaco', 378: 'San Marin', 380: 'Ukraine', 381: 'Serbie',
        382: 'Monténégro', 383: 'Kosovo', 385: 'Croatie', 386: 'Slovénie', 387: 'Bosnie-Herzégovine', 389: 'Macédoine',
        39: 'Italie', 40: 'Roumanie', 41:
            'Suisse', 420: 'République Tchèque', 421: 'Slovaquie', 423: 'Liechtenstein', 43: 'Autriche',
        44: 'Royaume-Uni', 45: 'Danemark', 46: 'Suède', 47: 'Norvège', 48: 'Pologne', 49: 'Allemagne', 501: 'Belize',
        502: 'Guatemala', 503: 'El Salvador', 504: 'Honduras', 505: 'Nicaragua', 506: 'Costa Rica', 507: 'Panama',
        509: 'Haïti', 51: 'Pérou', 52: 'Mexique', 54: 'Argentine', 55: 'Brésil', 56: 'Chili', 57: 'Colombie',
        58: 'Venezuela', 591: 'Bolivie', 592: 'Guyana', 593: 'Equateur', 595: 'Paraguay', 597: 'Suriname',
        598: 'Uruguay', 599: 'Antilles Néerlandaises', 60: 'Malaisie', 61: 'Iles Christmas', 61891: 'Iles Cocos',
        62: 'Indonésie', 63: 'Philippines'
    , 64: 'Nouvelle-Zélande', 643305: 'Iles Chatham', 65: 'Singapour', 66: 'Thaïlande', 673: 'Brunei', 676: 'Tonga',
        678: 'Vanuatu', 679: 'Fidji', 680: 'Palau', 681: 'Wallis-et-Futuna', 685: 'Samoa', 687: 'Nouvelle-Calédonie',
        689: 'Polynésie Française', 691: 'Micronésie', 692: 'Iles Marshall', 7: 'Russie', 77: 'Kazakhstan', 81: 'Japon',
        82: 'Corée du Sud', 84: 'Vietnam', 852: 'Hong Kong', 853: 'Macao', 855: 'Cambodge', 856: 'Laos', 86: 'Chine',
        880: 'Bangladesh', 886: 'Taïwan', 90: 'Turquie', 90392: 'Chypre Nord', 91: 'Inde', 92: 'Pakistan',
        93: 'Afghanistan', 94: 'Sri Lanka', 95: 'Myanmar', 960: 'Maldives', 961: 'Liban', 962: 'Jordanie', 963: 'Syrie',
        964: 'Irak', 965: 'Koweït', 966: 'Arabie Saoudite', 967: 'Yémen', 968: 'Oman', 970: 'Palestine',
        971: 'Emirats Arabes Unis', 972: 'Israël', 973: 'Bahreïn', 974: 'Qatar', 975: 'Bhoutan', 976: 'Mongolie',
        977: 'Népal', 98: 'Iran', 992: 'Tadjikistan', 993: 'Turkménistan', 994: 'Azerbaïdjan', 995: 'Géorgie',
        996: 'Kirghizistan', 998: 'Ouzbékistan'}

minute_indivisible = {682: ' Cook island ', 679: ' Fidji island ', 689: ' French Polynesia ', 509: ' Haiti ',
                      686: ' Kiribati ', 266: ' Lesotho ', 960: ' Maldives ', 674: ' Nauru ', 687: ' New Caledonia ',
                      683: ' Niue ', 675: ' Papua New Guinea ', 677: ' Salomon isl ', 1684: ' Samoa American ',
                      685: ' Samoa Western ', 597: ' Suriname',
                      690: ' Tokelau ', 676: ' Tonga ', 688: ' Tuvalu ', 678: ' Vanuatu ', 247: 'Ascension',
                      246: 'Diego Garcia', 809: 'Dominicaine Republique', 500: 'Falkland', 36: 'Hongrie',
                      691: 'Micronesie', 51: 'Perou', 378: 'San Marino'}

# For hvi
@st.experimental_memo
def hvi():
    df = pd.read_excel(uploaded_f, engine='openpyxl')
    df['h_appel'] = pd.to_datetime(df['h_appel'])

    df['first_range'] = df['num_ligne'].astype(str).str.replace('.', '').str[0:3]
    df['first_range'] = df['first_range'].astype(int)
    st.write(df['first_range'].dtype)
    # st.write([type(k) for k in pays.keys()])
    # for keys, value in pays.items():
    #     if keys in df['first_range']:
    #         df['checked'] = "True"
    #     else:
    #         df['checked'] = "False"

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
    generate_excel_download_link(hvi_dataframe)

    # Download function


