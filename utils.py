import base64
import streamlit as st
import pandas as pd
from PIL import ImageOps, Image
import numpy as np
import cv2
import random
from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.models import load_model, Model
from keras.layers import GlobalAveragePooling2D
import keras
import pickle
import joblib
#from streamlit_extras.app_logo import add_logo
from folium import GeoJson
import json

#-----------------------------------------------------------------------------#
# Set background
#-----------------------------------------------------------------------------#
def set_background(image_file):
    """
    This function sets the background of a Streamlit app to an image specified by the given image file.

    Parameters:
        image_file (str): The path to the image file to be used as the background.

    Returns:
        None
    """
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)

#-----------------------------------------------------------------------------#
# Create patches
#-----------------------------------------------------------------------------#
def createPatches(image, file):
    ## Prameters and lists save patches and labels
    patches = 50                                                     # Number of patches per image
    patchsize = 224                                                  # Patch size (224 x 224 pixels)
    scale_percent = 20                                               # scale image
    random.seed(42)                                                  # seed for reproducibility

    imgs = []                                                        # patches images list
    labels = []                                                      # patches labels list

    ## Resize image
    w = int(image.shape[1] * scale_percent / 100)                      # resize width
    h = int(image.shape[0] * scale_percent / 100)                      # resize height
    resized_image = cv2.resize(image, (w, h))                          # resize image based on w and h

    ## Extract 50 random patches (224 x 224)
    for i in range(patches):
      x = random.randrange(0, w-patchsize)
      y = random.randrange(0, h-patchsize)

      new_img = resized_image[y:y+patchsize, x:x+patchsize]          # crop image

      nfname = ("%d_%s" % (i, file.name))                            # new name for patches images
      #print(nfname)
      imgs.append(new_img)                                           # Add patches arrays to list
      labels.append((nfname))                                        # Add patches labels to list
    return np.array(imgs), np.array(labels)
    
#-----------------------------------------------------------------------------#
# Feature Extractor (ResNet50)
#-----------------------------------------------------------------------------#
@st.cache_resource(show_spinner = False)                               # 👈 Add the caching decorator
def featureExtractor():   
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    base_model.trainable = False
    inputs = keras.Input(shape = (224, 224, 3))
    x = preprocess_input(inputs)
    x = base_model(x)
    output = GlobalAveragePooling2D()(x)
    feature_extractor = Model(inputs, output)
    return feature_extractor

#-----------------------------------------------------------------------------#
# Extract Feature (ResNet50)
#-----------------------------------------------------------------------------#
def extractFeature(patches, feature_extractor):   
    feature = []
    for img in patches:
        img = np.expand_dims(img, 0)
        print(img.shape)
        X_features = feature_extractor.predict(img)
        feature.append(X_features)
        df = pd.DataFrame(np.concatenate(feature))
    return df

#-----------------------------------------------------------------------------#
# Load Classifier (ResNet50 extractor + SVC)
#-----------------------------------------------------------------------------#
@st.cache_resource(show_spinner = False)                               # 👈 Add the caching decorator
def classifier():
    model = pickle.load(open('./model/best_resnet_svc.pickle', "rb"))
    #model = joblib.load('./model/best_resnet_svc.joblib')
    return model

#-----------------------------------------------------------------------------#
# Class predicted and probabilities (patches)
#-----------------------------------------------------------------------------#

def predition(model, feature):
    y_pred = model.predict(feature)                                # Class predicted                       
    y_prob = model.predict_proba(feature)                          # Class probabilities
    y_prob = pd.DataFrame(y_prob, columns = model.classes_)
    class_value = y_prob.idxmax(axis = 1)
    prob_value = y_prob.max(axis = 1)
    prob_class = pd.DataFrame({'Predicted class': class_value,
                               'Class probabilities': prob_value})
    df = prob_class.groupby('Predicted class',  sort = False).agg(
        Mean = ('Class probabilities', 'mean'),
        Sum = ('Class probabilities', 'sum'))
    
    df = prob_class.groupby('Predicted class',  sort = False).agg(
        Patches = ('Predicted class', 'count'),
        Sum = ('Class probabilities', 'sum'),
        Mean = ('Class probabilities', 'mean')
    ).sort_values(by = 'Patches', ascending = False).head(3)
    
    df['Rank'] = range(1, len(df) + 1)

    return df

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: ./LMFTCA.png;
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "My Company Name";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Wide page config
def wide_space_default():
    st.set_page_config(layout='wide')

#-----------------------------------------------------------------------------#
# Load GeoJson
#-----------------------------------------------------------------------------#
@st.cache_resource(show_spinner = False)                               # 👈 Add the caching decorator
def Geojson():
    BRAZIL = './map/br_states.json'
    MUN = './map/MT.json'
    MT = './map/geojs-51-mun.json'
    
    file = open(MT, encoding = 'utf8')
    file2 = open(MUN, encoding = 'utf8')
    file3 = open(BRAZIL, encoding = 'utf8')
    
    text = file.read()
    text2 = file2.read()
    text3 = file3.read()

    list = [text, text2, text3]
    return list