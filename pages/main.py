import streamlit as st
import cv2
import numpy as np

from utils import (
    set_background,
    createPatches,
    featureExtractor,
    classifier,
    predition,
    extractFeature
)

#from util import set_background, createPatches, featureExtractor, Classifier, predition, extractFeature
from annotated_text import annotated_text, annotation

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

# Set background (config.toml)
set_background('./bgs/background.png')

# Insert image on sidebar
#images = ['./logo/LMFTCA.png', './logo/ufpa.png']
st.sidebar.image('./logo/image.png', use_column_width = True)
st.sidebar.write('Developed by:')
st.sidebar.markdown('[Deivison Venicio Souza (UFPA)](https://github.com/DeivisonSouza)')
st.sidebar.markdown('[Natally Celestino Gama (Forest Engineer)](https://github.com/DeivisonSouza)')

# Set title
st.markdown("<h3 style='text-align: left; color: darkgreen;'>🌳DEEP BARK APP       𓂃⋅𓂃⋅𓂃⋅𓂃⋅𓂃⋅𓂃⋅𓂃⋅</h3>", unsafe_allow_html=True)

#st.title(""" 👉 DEEP BARK WEB APP """)

# Set header
#st.header('(A System to Recognize Tree Species in Sustainable Forest Management, Amazon, Brazil)')
st.markdown("<h3 style='text-align: center; color: darkgreen;'>A System to Recognize Tree Species in Sustainable Forest Management Based on Bark Images, Amazon, Brazil</h3>", unsafe_allow_html=True)
#st.markdown("<h3 style='text-align: center; color: darkgreen;'>(Um Sistema para Reconhecer Espécies Arbóreas no Manejo Florestal Sustentável Baseado em Imagens de Casca, Amazônia, Brasil)</h3>", unsafe_allow_html=True)

st.markdown("""---""")

st.info(
"""
#### ⚠️**IMPORTANT!**

The model available in this system was trained to **recognize only 16 commercial wood species from the Brazilian Amazon** (see the list of species in '**Herbarium**' and bark samples in '**Bark Samples**'). If images of bark from other species are used, the system will classify the image as belonging to one of the 16 species (most likely the one with the greatest similarity). This alert is important, as users might present images of bark from other species to the system. Therefore, it is crucial to expand the set of images to include new species and increase the representativeness of specimens. This should take into account the various factors that can cause variations in the external bark of trees, aiming to build a more generalist model.

"""

)

# st.markdown(
# """
# ----------------------------------
# #### ⚠️**IMPORTANTE!**

# O modelo disponível nesse sistema foi treinado para reconhecer apenas 16 espécies comerciais madeireiras da Amazônia brasileira (ver lista de espécies em ‘Herbarium’ e as amostras de cascas em ‘Bark Samples’). No entanto, se imagens de cascas de outras espécies forem usadas, o sistema classificará a imagem como pertencente a alguma das 16 espécies (certamente aquela com maior semelhança). Este alerta é importante, pois é possível que usuários apresentem ao sistema imagens de casca de outras espécies. Portanto, isso reforça a necessidade de ampliação do conjunto de imagens, com inclusão de novas espécies e aumento da representatividade de espécimes, atendo-se aos diversos fatores que podem causar variações nas cascas externas das árvores, visando a construção de um modelo mais generalista.

# """
# )


st.markdown("""---""")

# Rown 1 ---------------------------------------------
col1, col2 = st.columns([0.6, 0.4], gap = "medium")

with col1:
  # upload image
  #  file = st.sidebar.file_uploader(label = 'Upload bark image',
  #                                  type = ['jpeg', 'png', 'jpg'],
  #                                  label_visibility = 'hidden')
   st.write('##### :blue[**Upload bark image**]👇')
   file = st.file_uploader(label = 'Upload bark image',
                           type = ['jpeg', 'png'],
                           label_visibility = 'hidden'
                           )
   
   #st.set_option('deprecation.showfileUploaderEncoding', False)

   if file is not None:
     # else:
     # st.write("Filename: ", file.name)                              # write filename
     f = file.read()                                                  # read image
     img = np.asarray(bytearray(f), dtype = np.uint8)                 # convert to numpy array
     img = cv2.imdecode(img, cv2.IMREAD_COLOR)                        # convert bytes to image format
     st.image(img, use_column_width = True, channels = 'BGR', width = 150)                                  # image display
       
     with col2:
       st.write('#####')
       classify = st.button('Recognize specie')  
       if classify:
         with st.spinner('Please wait! Extracting 50 patches from the image...'):
           # Extract patches
           patches, labels = createPatches(image = img, file = file)
           # st.write(f"Total patches: {len(patches)}")
           # st.write(f"Total labels: {len(labels)}")
        
         with st.spinner('Please wait! Applying the Feature Extractor to Patches (ResNet50)...'):
           # Feature Extractor (ResNet50)
           feature_extractor = featureExtractor()
           # st.write(f"Total labels: {feature}")

           # Extract Feature (ResNet50)
           feature = extractFeature(patches = patches, 
                              feature_extractor = feature_extractor)
        
         with st.spinner('Please wait! Making predictions on patches using the SVC model...'):
           # Load Classifier (ResNet50 extractor + SVC)
           model = classifier()

           # Class predicted and probabilities (patches)
           df = predition(model = model, feature = feature)
           
           class_predict = df['Sum'].idxmax()
           class_prob = df['Mean'].max()

           st.write("""# Image Classification""")
           #st.metric(label="👉The image is classified as:", value=class_predict, delta="")
           #st.write(f"👉The image is classified as: *:blue[{class_predict}]*")
           
           st.write(f"👉 The image is classified as belonging to the species: ")
           annotated_text("", annotation(class_predict, "", font_family="Comic Sans MS", border="2px dashed red"),)
           # st.write(f"👉 The class average probability is: *:blue[{round(class_prob, 5)}]*")
           #x = str(round(class_prob*100, 2)).format()
           x = f"{round(class_prob*100, 2):.2f}%"
           #st.write(f"👉 The class average probability is: *:blue[{class_prob*100:.2f}%]*")
           st.metric(label="👉 The (average) probability of the image belonging to the species is:", value=x, delta="")
           
           st.markdown("""---""")
           st.markdown("""**Summary - Predicted classes for patches.**""")
           
           st.dataframe(df.loc[:, df.columns != 'Mean'])
           
           #st.markdown("""Na tabela, estão listadas as classes (espécies) atribuídas para cada patch de imagem. A espécie ‘X’ foi atribuída à ‘X’ patches de um total de 50, com soma e média de probabilidades máximas igual a ‘y’ e ‘z’, respectivamente. Portanto, a imagem é classificada como pertencente a espécie ‘X’.""")
           st.write(
                  ':blue-background[The classes (species) assigned to each image patch are listed in the table. Species]', f" :red-background[:red[*{class_predict}*]]", ':blue-background[was assigned to] ', f":red-background[:red[*{df['Patches'][0]}*]]", ':red-background[:red[patches]] :blue-background[out of a total of 50, with sum and mean maximum probabilities equal to]', f":red-background[:red[*{round(df['Sum'][0],2)}*]]" ,':blue-background[and]', f":red-background[:red[*{x}*],]", ':blue-background[respectively. Therefore, the image is classified as belonging to species]', f":red-background[:red[*{class_predict}*]]", '.'
                  )
           
           #st.write('The classes (species) assigned to each image patch are listed in the table. Species ', f":blue[*{class_predict}*]" , 'was assigned to ', f":blue[*{df['Patches'][0]}*]", ':blue[patches] out of a total of 50, with sum and mean maximum probabilities equal to', f":blue[*{round(df['Sum'][0],2)}*]" ,'and', f":blue[*{x}*],", 'respectively. Therefore, the image is classified as belonging to species', f":blue[*{class_predict}*]", '.')
           
           st.markdown("""---""")
           st.write(f"**Patches** = The number of patches (each 256 x 256 pixels) classified as belonging to a specific class (species). The class of each patch is determined by the highest class probability value. ")
           st.write(f"**Sum** = The sum of the maximum probabilities of the predicted class.")
           st.write(f"**Rank** = The order of predicted classes (species) based on the highest sum of probabilities.")
           
           st.markdown("""---""")
# with col2:
#    st.write('')
#    st.write('')
#    st.write('')
#    st.write('')
#    st.write('')
#    st.write('')
#    st.write('As 3 espécies com maior probabilidade são:')

# Insert image on sidebar
# images = ['./logo/LMFTCA.png', './logo/ufpa.png']
# st.sidebar.image(images, use_column_width = True, width = 100)