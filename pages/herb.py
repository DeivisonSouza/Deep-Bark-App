import streamlit as st
import pandas as pd
from utils import set_background

st.set_page_config(#page_title = 'Home', 
                   #page_icon = "👋", 
                    layout = "wide", 
                    initial_sidebar_state= "auto")

# Reduce white space top of the page
st.markdown("""
        <style>
               .block-container {
                    padding-top: 5rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                    text-align: justify
                }
            
        </style>
        """, unsafe_allow_html=True)

# Set background (config.toml)
set_background('./bgs/background.png')

# Insert image on sidebar
#images = ['./logo/LMFTCA.png', './logo/ufpa.png']
st.sidebar.image('./logo/image.png', use_column_width = True)
st.sidebar.write('Developed by:')
st.sidebar.markdown('[Deivison Venicio Souza (UFPA)](https://github.com/DeivisonSouza)')
st.sidebar.markdown('[Natally Celestino Gama (Forest Engineer)](https://github.com/DeivisonSouza)')

# Load table (HFC)
df = pd.read_excel('./herbario/HFC-UFRA-RESUMO.xlsx', index_col = 0)
st.markdown("<h3 style='text-align: left; color: darkgreen;'>🌳HERBARIUM DATA       𓂃⋅𓂃⋅𓂃⋅𓂃⋅𓂃⋅𓂃⋅𓂃⋅</h3>", unsafe_allow_html=True)
#st.title(""" 👉 Herbarium Data """)
st.markdown("<h3 style='text-align: center; color: darkgreen;'>Identification of Botanical Material - Felisberto Camargo Herbarium (HFC) of Federal Rural University of the Amazon</h3>", unsafe_allow_html=True)
#st.markdown("<h3 style='text-align: left; color: darkgreen;'>(Identification of Botanical Material - Felisberto Camargo Herbarium (HFC) of Federal Rural University of the Amazon - UFRA)</h3>", unsafe_allow_html=True)
st.markdown("""---""")
#st.markdown("""#####""")
#st.markdown("""🌲🌳🌿‧₊˚ ⋅🌿🌱𓂃 ࣪ ִֶָ.🌲🌳🌿‧₊˚ ⋅""")
#st.markdown("Identificação de material botânico realizada no Herbário Felisberto Camargo (HFC) da Universidade Federal Rural da Amazônia (UFRA).")
st.write(df)
#st.markdown("""🌲🌳🌿‧₊˚ ⋅🌿🌱𓂃 ࣪ ִֶָ.🌲🌳🌿‧₊˚ ⋅""")