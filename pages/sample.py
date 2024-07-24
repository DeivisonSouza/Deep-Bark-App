import streamlit as st
from PIL import Image
import cv2
import numpy as np
from st_pages import show_pages_from_config, add_page_title

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

# Set background-color sidebar
st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: #e1d3bf;
        }
    </style>
    """, unsafe_allow_html=True)

# Insert image on sidebar
#images = ['./logo/LMFTCA.png', './logo/ufpa.png']
st.sidebar.image('./logo/image.png', use_column_width = True)
st.sidebar.write('Developed by:')
st.sidebar.markdown('[Deivison Venicio Souza (UFPA)](https://github.com/DeivisonSouza)')
st.sidebar.markdown('[Natally Celestino Gama (Forest Engineer)](https://github.com/DeivisonSouza)')

# Set sidebar (title and icon) - (pages.toml)
#add_page_title()
#show_pages_from_config()

# Set title
st.markdown("<h3 style='text-align: left; color: darkgreen;'>🌳BARK IMAGES       𓂃⋅𓂃⋅𓂃⋅𓂃⋅𓂃⋅𓂃⋅𓂃⋅</h3>", unsafe_allow_html=True)

# Set header
#st.header('(A System to Recognize Tree Species in Sustainable Forest Management, Amazon, Brazil)')
st.markdown("<h3 style='text-align: center; color: darkgreen;'>Sample of images of bark from 16 tree species managed in the Brazilian Amazon</h3>", unsafe_allow_html=True)
#st.markdown("<h3 style='text-align: left; color: darkgreen;'>(Sample of images of bark from 16 tree species managed in the Brazilian Amazon)</h3>", unsafe_allow_html=True)

st.markdown("""---""")

# Rown 1 ---------------------------------------------
col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Apuleia leiocarpa </em> <br> <strong>Author:</strong> (Vogel) J. F. Macbr. <br> <strong>Family:</strong> Fabaceae <br> <strong>Local:</strong> Nova Maringá/MT <br> <strong>Lat:</strong> 12.6959 <br> <strong>Long:</strong> 57.24636 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/NM_01_R_11_C_4.jpg')
   st.image('./sample/NM_01_R_11_C_4.jpg')

with col2:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Astronium lecointei </em> <br> <strong>Author:</strong> Ducke <br> <strong>Family:</strong> Anacardiaceae <br> <strong>Local:</strong> Cotriguaçu/MT <br> <strong>Lat:</strong> 9.82936 <br> <strong>Long:</strong> 58.30251 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/CO_02_R_127_C_7.jpg')
   st.image('./sample/CO_02_R_127_C_7.jpg')

with col3:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Bagassa guianensis </em> <br> <strong>Author:</strong> Aubl. <br> <strong>Family:</strong> Moraceae <br> <strong>Local:</strong> Cotriguaçu/MT <br> <strong>Lat:</strong> 9.82928 <br> <strong>Long:</strong> 58.30232 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/CO_03_R_128_C_5.jpg')
   st.image('./sample/CO_03_R_128_C_5.jpg')

with col4:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Bowdichia nitida </em> <br> <strong>Author:</strong> Spruce ex Benth. <br> <strong>Family:</strong> Fabaceae <br> <strong>Local:</strong> Feliz Natal/MT <br> <strong>Lat:</strong> 12.36177 <br> <strong>Long:</strong> 54.86732 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/FN_04_R_109_C_2.jpg')
   st.image('./sample/FN_04_R_109_C_2.jpg')

st.markdown("""---""")
# Rown 2 ---------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Cedrela odorata</em> <br> <strong>Author:</strong> L. <br> <strong>Family:</strong> Meliaceae <br> <strong>Local:</strong> Cotriguaçu/MT <br> <strong>Lat:</strong> 9.82739 <br> <strong>Long:</strong> 58.29147 </p>'
   #new_title = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 14px;"> <em>Cedrela odorata</em> L.</p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/CO_05_R_159_C_5.jpg')
   st.image('./sample/CO_05_R_159_C_5.jpg')

with col2:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Dipteryx odorata</em> <br> <strong>Author:</strong> (Aubl.) <br> <strong>Family:</strong> Fabaceae <br> <strong>Local:</strong> Nova Maringá/MT <br> <strong>Lat:</strong> 12.694 <br> <strong>Long:</strong> 57.24681 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/NM_06_R_3_C_5.jpg')
   st.image('./sample/NM_06_R_3_C_5.jpg')

with col3:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Erisma uncinatum</em> <br> <strong>Author:</strong> Warm. <br> <strong>Family:</strong> Voschysiaceae <br> <strong>Local:</strong> Nova Maringá/MT <br> <strong>Lat:</strong> 12.69693 <br> <strong>Long:</strong> 57.24626 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/NM_07_R_13_C_2.jpg')
   st.image('./sample/NM_07_R_13_C_2.jpg')

with col4:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Goupia glabra</em> <br> <strong>Author:</strong> Aubl. <br> <strong>Family:</strong> Goupiaceae <br> <strong>Local:</strong> Feliz Natal/MT <br> <strong>Lat:</strong> 12.36386 <br> <strong>Long:</strong> 54.81213 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/FN_08_R_77_C_5.jpg')
   st.image('./sample/FN_08_R_77_C_5.jpg')

st.markdown("""---""")
# Rown 3 ---------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Hymenolobium petraueum</em> <br> <strong>Author:</strong> Ducke <br> <strong>Family:</strong> Fabaceae <br> <strong>Local:</strong> Feliz Natal/MT <br> <strong>Lat:</strong> 12.35629 <br> <strong>Long:</strong> 54.81459 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/FN_09_R_75_C_4.jpg')
   st.image('./sample/FN_09_R_75_C_4.jpg')

with col2:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Mezilaurus itaúba</em> <br> <strong>Author:</strong> (Meisn.) Taub. ex Mez <br> <strong>Family:</strong> Lauraceae <br> <strong>Local:</strong> Nova Maringá/MT <br> <strong>Lat:</strong> 12.6976 <br> <strong>Long:</strong> 57.24608 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/NM_10_R_14_C_7.jpg')
   st.image('./sample/NM_10_R_14_C_7.jpg')

with col3:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Parkia pendula</em> <br> <strong>Author:</strong> (Willd) Benth. Ex Walp. <br> <strong>Family:</strong> Fabaceae <br> <strong>Local:</strong> Feliz Natal/MT <br> <strong>Lat:</strong> 12.36579 <br> <strong>Long:</strong> 54.81199 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/FN_11_R_88_C_7.jpg')
   st.image('./sample/FN_11_R_88_C_7.jpg')

with col4:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Protium acrense</em> <br> <strong>Author:</strong> Daly <br> <strong>Family:</strong> Burseraceae <br> <strong>Local:</strong> Cotriguaçu/MT <br> <strong>Lat:</strong> 9.82955 <br> <strong>Long:</strong> 58.29076 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/CO_12_R_151_C_5.jpg')
   st.image('./sample/CO_12_R_151_C_5.jpg')

st.markdown("""---""")
# Rown 4 ---------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Qualea paraensis</em> <br> <strong>Author:</strong> Ducke <br> <strong>Family:</strong> Voschysiaceae <br> <strong>Local:</strong> Nova Maringá/MT <br> <strong>Lat:</strong> 12.68625 <br> <strong>Long:</strong> 57.22785 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/NM_13_R_45_C_4.jpg')
   st.image('./sample/NM_13_R_45_C_4.jpg')

with col2:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Simarouba amara</em> <br> <strong>Author:</strong> Aubl. <br> <strong>Family:</strong> Simaroubaceae <br> <strong>Local:</strong> Cotriguaçu/MT <br> <strong>Lat:</strong> 9.82924 <br> <strong>Long:</strong> 58.29611 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/CO_14_R_123_C_1.jpg')
   st.image('./sample/CO_14_R_123_C_1.jpg')

with col3:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Trattinnickia burserifolia</em> <br> <strong>Author:</strong> Mart. <br> <strong>Family:</strong> Burseraceae <br> <strong>Local:</strong> Feliz Natal/MT <br> <strong>Lat:</strong> 12.36442 <br> <strong>Long:</strong> 54.81253 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/FN_15_R_79_C_5.jpg')
   st.image('./sample/FN_15_R_79_C_5.jpg')

with col4:
   new_title = '<p style="font-family:sans-serif; text-align: left; color:Green; font-size: 10px;"> <strong> Specie: </strong> <em> Vatairea sericea</em> <br> <strong>Author:</strong>  (ducke) Ducke <br> <strong>Family:</strong> Fabaceae <br> <strong>Local:</strong> Nova Maringá/MT <br> <strong>Lat:</strong> 12.69115 <br> <strong>Long:</strong> 57.24829 </p>'
   st.markdown(new_title, unsafe_allow_html = True)
   #image = Image.open('./sample/NM_16_R_57_C_4.jpg')
   st.image('./sample/NM_16_R_57_C_4.jpg')
   
st.markdown("""---""")