import streamlit as st
from utils import set_background
from st_pages import show_pages_from_config, add_page_title
from PIL import Image
#from streamlit_extras.app_logo import add_logo

# Set page (title and icon)
st.set_page_config(page_title = 'Home', 
                    page_icon = "👋", 
                    layout = "wide", 
                    initial_sidebar_state= "auto")

# Set background-color sidebar
st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: #e1d3bf;
        }
    </style>
    """, unsafe_allow_html=True)

# Logo
#add_logo("./assets/images/LMFTCA.png", height=200)

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

# Set background (config.toml)
set_background('./bgs/background.png')

# Insert image on sidebar
#logo()
#st.sidebar.image("./logo/LMFTCA.png", use_column_width=True)

# Set sidebar (title and icon) - (pages.toml)
# add_page_title()
show_pages_from_config()

# Set title page
#st.write("# Seja bem vindo(a)! 👋")
st.write("# Welcome! 👋")

#st.sidebar.success("Select a option above.")

# Contextualização
#st.title(""" 👉 SOBRE A APLICAÇÃO WEB """)
st.markdown("<h5 style='text-align: left; color: darkgreen;'>🌳DEEP BARK PROJECT</h5>", unsafe_allow_html=True)
#st.markdown("#### 🌳:green[DEEP BARK PROJECT]")
#st.subheader("🌳:green[DEEP BARK PROJECT]")

# st.markdown(
# """
# ----------------------------------
# #### 🔎**CONTEXTUALIZAÇÃO**

# No âmbito do Manejo Florestal Sustentável - MFS para fins madeireiros, o inventário florestal 100% - IF100% (ou censo florestal) é uma atividade pré-exploratória fundamental para identificação do potencial produtivo da floresta, regulação da produção florestal e definição de estratégias operacionais nas etapas exploratórias e pós-exploratórias. Por meio do IF100%, as árvores de interesse econômico (e de valor potencial) e com diâmetro mínimo pré-estabelecido são descobertas na floresta, recebem uma placa de identificação, têm sua localização definida com auxílio de GPS (do inglês, Global Positioning System – GPS) e comumente são identificadas por nomes vernaculares. 

# A identificação de espécies da flora é sem dúvida um dos principais desafios do censo florestal no âmbito do Manejo Florestal Sustentável - MFS para fins madeireiros, pois não é incomum a ocorrência de erros. Esses erros podem ter origem no campo, pela confusão devido ao compartilhamento de características entre espécies, uso de diferentes nomes vernaculares para identificar uma mesma espécie, ou mesmo pelo uso do mesmo nome vernacular para identificar espécies distintas. Ademais, não existe a obrigatoriedade e nem a preocupação de realização de coletas botânicas para confirmação da espécie. Soma-se a isso, os erros graves ocasionados pela conversão de nomes vernaculares para nomes científicos, baseado em listas pré-existentes de orgãos ambientais. 

# Procópio e Secco (2008), reportaram agrupamento de espécies ao estudarem a identificação de árvores denominadas “Tauari” em áreas manejadas nos pólos madeireiros central e leste do Estado do Pará. Por exemplo, no pólo central, Couratari guianensis agruparam três espécies: *Couratari guianensis*, *C. oblongifolia* e *C. stellata*. Lacerda e Nimmo (2010), também reportaram que 43,5% (132 espécies) de todas as espécies identificadas por descrição botânica, não constavam na identificação de árvores realizada no IF-100%. 

# Nesse contexto, emergiu o **"Projeto Deep Bark – Aprendizado Profundo para Reconhecer Espécies de Árvores no Manejo Florestal Madeireiro na Amazônia Brasileira"**, cujo objetivo foi desenvolver uma aplicação web, baseada em inteligência artificial e visão computacional, para reconhecer árvores de espécies de valor comercial em censos florestais, no âmbito do MFS para fins madeireiros. O classificador disponibilizado nesta aplicação web possui acurácia estimada de 95% e pode ser usado para reconhecer 16 espécies de valor comercial madeireiro (ver lista de espécies). 

# Esta aplicação pode ser usada como uma ferramenta auxiliar na identificação de árvores no MFS para fins madeireiros, por identificadores botânicos, técnicos de órgãos ambientais e leigos. Destarte, espera-se contribuir para o aumento da acurácia na identificação de espécies, em especial, daquelas mais confundidas e, por conseguinte, minimizar os impactos ecológicos e econômicos originados pelos erros de identificação de espécies no IF100%. Por fim, esta tecnologia tem potencial para contribuir no refinamento da identificação de espécies em diferentes regiões da Amazônia.
# """
# )

st.markdown(
"""
----------------------------------
##### 🔎**CONTEXTUALIZATION**

Within the scope of Sustainable Forest Management (SFM) for timber purposes, the 100% forest inventory (IF100%), also known as the forest census, is a fundamental pre-exploratory activity. It is essential for identifying the productive potential of the forest, regulating forest production, and defining operational strategies for both exploratory and post-exploratory stages. Through IF100%, trees of economic interest (and potential value) with a pre-established minimum diameter are identified in the forest. These trees receive an identification plate, their locations are determined using GPS (Global Positioning System), and they are commonly identified by their vernacular names.

The identification of flora species is undoubtedly one of the main challenges of the forest census within the scope of SFM for timber purposes, as errors are not uncommon. These errors may originate in the field due to the confusion caused by shared characteristics between species, the use of different vernacular names to identify the same species, or even the use of the same vernacular name to identify different species. Furthermore, there is no obligation or concern to carry out botanical collections to confirm the species. This issue is compounded by serious errors that arise from converting vernacular names to scientific names, which are often based on pre-existing lists from environmental bodies.

Procópio and Secco (2008) reported the grouping of species when studying the identification of trees called "Tauari" in managed areas in the central and eastern logging poles of the State of Pará. For example, in the central pole, *Couratari guianensis* grouped three species: *Couratari guianensis*, *C. oblongifolia*, and *C. stellata*. Lacerda and Nimmo (2010) also reported that 43.5% (132 species) of all species identified by botanical description were not included in the tree identification carried out in the IF-100%.

In this context, the "**Deep Bark Project – Deep Learning to Recognize Tree Species in Timber Forest Management in the Brazilian Amazon**" emerged. The objective of this project was to develop a web application, based on artificial intelligence and computer vision, to recognize trees of commercially valuable species in forest censuses, within the scope of SFM for timber purposes. **The classifier available in this web application has an estimated accuracy of 95% and can be used to recognize 16 species of commercial timber value.**

This application can serve as an auxiliary tool for identifying trees in the SFM for logging purposes. It can be used by botanical identifiers, environmental agency technicians, and laypeople. It is expected to enhance accuracy in species identification, particularly for commonly misidentified species, thus minimizing the ecological and economic impacts of identification errors in IF100%. Ultimately, this technology has the potential to improve species identification across various regions of the Amazon.
"""
)

# Conjunto de imagens
st.markdown(
"""
-----------------------------------------
##### 📷**AMAZON BARK DATASET**

The bark images (rhytidome) were collected from three SFM Demonstration Units designated for timber purposes. These units are located in three municipalities in the state of Mato Grosso, Brazil: i) Fazenda Pérola in Nova Maringá, ii) Fazenda Boa Esperança in Feliz Natal, and iii) Fazenda São Nicolau in Cotriguaçu. 

In the field, images of the bark (rhytidome) of 10 trees per species were collected using two devices: a Canon camera and an iOS iPhone 11. The images were obtained with resolutions of 3024 x 4032 and 4000 x 5328, respectively. They were captured at heights ranging from 30 cm to 1.40 m above the ground and from a distance of 20 cm to 40 cm from the tree trunk.

The set of images, called Amazon Bark, consists of **2,803 images captured from 160 specimens belonging to 16 species, 16 genera, and 9 families**. Species identification was carried out by a parabotanist who climbed at least 5 trees per species to collect botanical material, including leaves, flowers, seeds, and fruits (though not all trees had all these structures). The sampling included 83 specimens from the 16 species.

The botanical material was sent to the Felisberto Camargo Herbarium (HFC) of the Federal Rural University of Amazonia (UFRA) for identification validation and registration. More details about the collection methodology and other relevant information can be found in **Natally Celestino Gama's** Master's thesis, “**Automatic recognition of Amazonian forest species from bark images based on local binary patterns and deep learning**”. To view sample bark images from the 16 species, refer to the **Bark Sample** menu.
"""
)
st.write("👉 **Master's thesis**[📓](https://ppgbc.propesp.ufpa.br/ARQUIVOS/dissertacoes/2024/Natally_Celestino_07.06.24.pdf)")

# st.markdown(
# """
# ----------------------------------
# #### 📷**CONJUNTO DE IMAGENS (AMAZON BARK DATASET)**

# As imagens de casca (ritidoma) foram coletadas em três Unidades Demonstrativas (UDs) de Manejo Florestal Sustentável (MFS) para fins madeireiro, localizadas em três municípios do estado do Mato Grosso, Brasil: i) Fazenda Pérola – Nova Maringá; ii) Fazenda Boa Esperança – Feliz Natal; e ii) Fazenda São Nicolau – Cotriguaçu. 

# Em campo, foram coletadas imagens de cascas (ritidoma) de 10 árvores por espécie, usando dois dispositivos: uma câmera Canon e um dispositivo iOS iPhone 11, obtendo imagens com resoluções de 3024 x 4032 e 4000 x 5328, respectivamente. As imagens foram capturadas em uma faixa de altura de 30 cm a 1,40 m de altura do solo e uma distância entre 20cm e 40cm do tronco da árvore. 

# O conjunto de imagens foi denominado **Amazon Bark**, composta por 2.803 imagens capturadas de 160 espécimes, pertencentes a 16 espécies, 16 gêneros e 9 famílias. A identificação de espécies foi realizada por um Parabotânico, que realizou a escalada de no mínimo 5 árvores por espécie para coleta de material botânico (folhas, flores, sementes e frutos – alguns não tinham todas as estruturas), com amostragem de 83 espécimes de 16 espécies.

# O material botânico foi enviado para o Herbário Felisberto Camargo (HFC) da Universidade Federal Rural da Amazônia (UFRA) para validação da identificação e registro. Mais detalhes sobre a metodologia de coleta e outras informações podem ser consultadas na dissertação de Mestrado de **Natally Celestino Gama**: **“Reconhecimento automático de espécies florestais amazônicas a partir de imagens de cascas baseado em padrões binários locais e aprendizado profundo”**. Veja o menu **Bark Sample** para visualizar amostras de imagens de cascas das 16 espécies.
# """
# )
# st.write("👉 **Acesse a Dissertação**[📓](https://github.com/DeivisonSouza)")

# Modelo de Reconhecimento

st.markdown(
"""
----------------------------------
##### 🤖**RECOGNITION MODEL**

This web application uses a classifier (with an estimated accuracy of 95%) learned using the Support Vector Machine (SVM) algorithm and ResNet50, a pre-trained Convolutional Neural Network (CNN), as a feature extractor from digital images of tree bark. The approach of using pre-trained networks is known as Transfer Learning. The model predictions follow these steps:
- **1 - Resizing**: High-resolution images are resized by 20%;
- **2 - Patches Extraction**: 50 patches of size 224 x 224 are randomly extracted from each original image;
- **3 - Pre-processing**: Applies the pre-processing steps defined by the pre-trained ResNet50 network to the 50 patches;
- **4 - Feature Extraction**: Utilizes the ResNet50 model with ImageNet weights and all convolutional layers frozen to extract features from the 50 patches; and
- **5 - Classification**: Employs a classifier trained on the **“Amazon Bark”** dataset to predict the class probability for each patche. A majority vote strategy, based on the sum of maximum class probabilities, is then applied to estimate the highest average class probability. Note that the classifier is currently configured to predict up to 16 classes. Future efforts will focus on expanding the image collection, including new species, to enhance specimen representativeness. This expansion will account for various factors influencing bark variations across tree species.
"""
)

# st.markdown(
# """
# ----------------------------------
# #### 🌳**MODELO DE RECONHECIMENTO**

# Esta aplicação web utiliza um classificador (acurácia estimada de 95%) aprendido usando o algoritmo Máquina de Vetores de Suporte (MVS) e ResNet50 - uma Rede Neural Convolucional (RNC) pré-treinada - como extrator de características das imagens digitais das cascas das árvores. A abordagem de usar redes pré-treinadas é conhecido como Aprendizado por Transferência (do inglês, Transfer Learning). As predições do modelo seguem as seguintes etapas:
# - **1 - Redimensionamento**: As imagens de alta resolução são redimensionadas na proporção de 20%;
# - **2 - Extração de subimagens**: São extraídas aleatoriamente 50 subimagens (patches) de tamanho 224 x 224 da imagem original;
# - **3 - Pré-processamento**: Aplica o pré-processamento da rede pré-treinada ResNet50 sobre as 50 subimagens;
# - **4 - Extração de características**: Usa o modelo ResNet50 - com pesos do ImageNet e todas as camadas convulacionais congeladas - para extrair características das 50 subimagens; e
# - **5 - Classificação**: Usa o classificador treinado sobre o conjunto de imagens **“Amazon Bark”** para predizer a probabilidade de classe cada subimagem e, na sequência, aplica a estratégia de voto majoritário, baseado na soma das máximas probabilidades de classes, para estimar a classe de maior probabilidade média. É importante lembrar que o classificador pode prever, a priori, apenas 16 classes. No futuro, novas coletas serão realizadas para ampliação do conjunto de imagens, com inclusão de novas espécies e aumento da representatividade de espécimes, atendo-se aos diversos fatores que podem causar variações nas cascas externas das árvores.
# """
# )

# Projeto e Equipe

st.markdown(
"""
----------------------------------
##### 👨🏻‍💻**PROJECT AND TEAM**

The project began in July 2022, with the signing of a Cooperation Agreement between the **Center for Wood-Producing and Exporting Industries of the State of Mato Grosso (CIPEM)**, the project financier, and the **Federal University of Pará (UFPA)**, with administrative and financial intervention by the **Research Support and Development Foundation (FADESP)**.

The project has a team of experts from four institutions:

- Prof. Dr. Deivison Venicio Souza (UFPA) - Coordinator (deivisonvs@ufpa.br)/[📄](http://lattes.cnpq.br/9063094443073532)/[🆔](https://orcid.org/0000-0002-2975-0927)
- Prof. Dr. Samuel de Pádua Chaves e Carvalho (UFRRJ) - (samuel.carvalho@ufrrj.br)/[📄](http://lattes.cnpq.br/6176482316661283)/[🆔](https://orcid.org/0000-0002-5590-9049)
- Prof. Dr. Eduardo da Silva Leal (UFRA) - (eduardo.leal@ufra.edu.br)/[📄](http://lattes.cnpq.br/1968764406721519)/[🆔]()
- Prof. Dr. Luiz Eduardo Soares de Oliveira (UFPR) - (Luiz.oliveira@ufpr.br)/[📄](http://lattes.cnpq.br/8607171759049558)/[🆔](https://orcid.org/0000-0002-0595-5370)
- Profa. Dra. Márcia Orie de Sousa Hamada (UFPA) - (marciahamada@ufpa.br)/[📄](http://lattes.cnpq.br/9880180163595986)/[🆔]()
- Natally Celestino Gama (Forest Engineer) - (natallygama28@gmail.com)/[📄](http://lattes.cnpq.br/6493402735030303)/[🆔](https://orcid.org/0000-0001-5131-9220)
----------------------------------
"""
)

# st.markdown(
# """
# ----------------------------------
# #### 👨🏻‍💻**PROJETO E EQUIPE**

# O projeto teve início em julho de 2022, pela firmação de Convênio de Cooperação entre o **Centro das Indústrias Produtoras e Exportadoras de Madeira do Estado do Mato Grosso (CIPEM)**, financiador do projeto, e a **Universidade Federal do Pará (UFPA)**, com interveniência administrativa e financeira da **Fundação de Amparo e Desenvolvimento da Pesquisa (FADESP)**. 

# O projeto possui uma equipe de especialistas de quatro instituições:

# - Prof. Dr. Deivison Venicio Souza (UFPA) - Coordenador (deivisonvs@ufpa.br)
# - Prof. Dr. Samuel de Pádua Chaves e Carvalho (UFRRJ) - (samuel.carvalho@ufrrj.br)
# - Prof. Dr. Eduardo da Silva Leal (UFRA) - (eduardo.leal@ufra.edu.br)
# - Prof. Dr. Luis Eduardo Soares Oliveira (UFPR) - (Luiz.oliveira@ufpr.br)
# - Profa. Dra. Márcia Orie de Souza Hamada (UFPA) - (marciahamada@ufpa.br)
# - Natally Celestino Gama (Engenheira Florestal) - (natallygama28@gmail.com)

# ----------------------------------
# """
# )

# Logo (Instituições envolvidas)
# Rown 1 ---------------------------------------------

st.markdown(
"""
##### 🏫**INSTITUITIONS**
"""
)

col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
   image = Image.open('./logo/UFPA.png')
   new_image = image.resize((200, 250))
   st.image(new_image)

with col2:
   image = Image.open('./logo/UFRRJ.png')
   new_image = image.resize((180, 230))
   st.image(new_image)

with col3:
   image = Image.open('./logo/UFRA.png')
   new_image = image.resize((220, 270))
   st.image(new_image)

with col4:
   image = Image.open('./logo/UFPR.png')
   new_image = image.resize((200, 250))
   st.image(new_image)

# Insert image on sidebar
#images = ['./logo/LMFTCA.png', './logo/ufpa.png']
st.sidebar.image('./logo/image.png', use_column_width = True)
st.sidebar.write('Developed by:')
st.sidebar.markdown('[Deivison Venicio Souza (UFPA)](https://github.com/DeivisonSouza)')
st.sidebar.markdown('[Natally Celestino Gama (Forest Engineer)](https://github.com/DeivisonSouza)')
