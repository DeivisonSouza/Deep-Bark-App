import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
from folium import plugins
from folium import GeoJson
import json
from utils import Geojson
from utils import set_background

st.set_page_config(#page_title = 'Home', 
                   #page_icon = "👋", 
                    layout = "wide", 
                    initial_sidebar_state= "auto")

# Reduce white space top of the page
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                    text-align: justify
                }
            
        </style>
        """, unsafe_allow_html=True)

#!pip install folium
#!pip install streamlit-folium

# Set background (config.toml)
set_background('./bgs/background.png')

# Insert image on sidebar
#images = ['./logo/LMFTCA.png', './logo/ufpa.png']
st.sidebar.image('./logo/image.png', use_column_width = True)
st.sidebar.write('Developed by:')
st.sidebar.markdown('[Deivison Venicio Souza (UFPA)](https://github.com/DeivisonSouza)')
st.sidebar.markdown('[Natally Celestino Gama (Forest Engineer)](https://github.com/DeivisonSouza)')
#st.markdown("""---""")

# Load table (HFC)
df = pd.read_excel('./herbario/HFC-UFRA-RESUMO.xlsx', index_col = 0)
#st.title(""" 👉 Location of trees - Mato Grosso, Brazil""")
st.markdown("<h3 style='text-align: left; color: darkgreen;'>🌳LOCATION OF TREES       𓂃⋅𓂃⋅𓂃⋅𓂃⋅𓂃⋅𓂃⋅𓂃⋅</h3>", unsafe_allow_html=True)
st.markdown("""---""")

df['LAT'] *= -1
df['LONG'] *= -1

map = folium.Map(location = [-15.5989, -56.0949], 
                 zoom_start = 5, 
                 control_scale = True)

map.add_child(folium.LatLngPopup())

# Load files Geojson
Geo = Geojson()

# Add map
folium.GeoJson(Geo[0], style_function = lambda x:{'fillColor': 'blue', 'color': 'white', 'weight': 0.5}).add_to(map)
folium.GeoJson(Geo[1], style_function = lambda x:{'fillColor': 'red', 'color': 'red', 'weight': 0.5}).add_to(map)
folium.GeoJson(Geo[2], style_function = lambda x:{'fillColor': 'orange', 'color': 'orange', 'weight': 0.5}).add_to(map)

# Add localization (trees)
for scientific, lat, lon in zip(df['SCIENTIFIC NAME'], df.LAT.values, df.LONG.values):
    folium.Marker([lat, lon], tooltip=f"{scientific}", icon=folium.Icon(icon = 'glyphicon glyphicon-tree-deciduous',
                                                                        color = 'green',
                                                                        icon_color = 'darkgreen',
                                                                        prefix = 'glyphicon')).add_to(map)

st_data = st_folium(map, width="1000", height="700")

st.markdown("""---""")