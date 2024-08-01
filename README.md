# Deep Bark App

###### 🔎**CONTEXTUALIZATION**

Within the scope of Sustainable Forest Management (SFM) for timber purposes, the 100% forest inventory (IF100%), also known as the forest census, is a fundamental pre-exploratory activity. It is essential for identifying the productive potential of the forest, regulating forest production, and defining operational strategies for both exploratory and post-exploratory stages. Through IF100%, trees of economic interest (and potential value) with a pre-established minimum diameter are identified in the forest. These trees receive an identification plate, their locations are determined using GPS (Global Positioning System), and they are commonly identified by their vernacular names.

The identification of flora species is undoubtedly one of the main challenges of the forest census within the scope of SFM for timber purposes, as errors are not uncommon. These errors may originate in the field due to the confusion caused by shared characteristics between species, the use of different vernacular names to identify the same species, or even the use of the same vernacular name to identify different species. Furthermore, there is no obligation or concern to carry out botanical collections to confirm the species. This issue is compounded by serious errors that arise from converting vernacular names to scientific names, which are often based on pre-existing lists from environmental bodies.

Procópio and Secco (2008) reported the grouping of species when studying the identification of trees called "Tauari" in managed areas in the central and eastern logging poles of the State of Pará. For example, in the central pole, *Couratari guianensis* grouped three species: *Couratari guianensis*, *C. oblongifolia*, and *C. stellata*. Lacerda and Nimmo (2010) also reported that 43.5% (132 species) of all species identified by botanical description were not included in the tree identification carried out in the IF-100%.

In this context, the "**Deep Bark Project – Deep Learning to Recognize Tree Species in Timber Forest Management in the Brazilian Amazon**" emerged. The objective of this project was to develop a web application, based on artificial intelligence and computer vision, to recognize trees of commercially valuable species in forest censuses, within the scope of SFM for timber purposes. **The classifier available in this web application has an estimated accuracy of 95% and can be used to recognize 16 species of commercial timber value.**

This application can serve as an auxiliary tool for identifying trees in the SFM for logging purposes. It can be used by botanical identifiers, environmental agency technicians, and laypeople. It is expected to enhance accuracy in species identification, particularly for commonly misidentified species, thus minimizing the ecological and economic impacts of identification errors in IF100%. Ultimately, this technology has the potential to improve species identification across various regions of the Amazon.

###### 📷**AMAZON BARK DATASET**

The bark images (rhytidome) were collected from three SFM Demonstration Units designated for timber purposes. These units are located in three municipalities in the state of Mato Grosso, Brazil: i) Fazenda Pérola in Nova Maringá, ii) Fazenda Boa Esperança in Feliz Natal, and iii) Fazenda São Nicolau in Cotriguaçu. 

In the field, images of the bark (rhytidome) of 10 trees per species were collected using two devices: a Canon camera and an iOS iPhone 11. The images were obtained with resolutions of 3024 x 4032 and 4000 x 5328, respectively. They were captured at heights ranging from 30 cm to 1.40 m above the ground and from a distance of 20 cm to 40 cm from the tree trunk.

The set of images, called Amazon Bark, consists of **2,803 images captured from 160 specimens belonging to 16 species, 16 genera, and 9 families**. Species identification was carried out by a parabotanist who climbed at least 5 trees per species to collect botanical material, including leaves, flowers, seeds, and fruits (though not all trees had all these structures). The sampling included 83 specimens from the 16 species.

The botanical material was sent to the Felisberto Camargo Herbarium (HFC) of the Federal Rural University of Amazonia (UFRA) for identification validation and registration. More details about the collection methodology and other relevant information can be found in **Natally Celestino Gama's** Master's thesis, “**Automatic recognition of Amazonian forest species from bark images based on local binary patterns and deep learning**”. To view sample bark images from the 16 species, refer to the **Bark Sample** menu.

👉 **Master's thesis**[📓](https://ppgbc.propesp.ufpa.br/ARQUIVOS/dissertacoes/2024/Natally_Celestino_07.06.24.pdf)

###### 🤖**RECOGNITION MODEL**

This web application uses a classifier (with an estimated accuracy of 95%) learned using the Support Vector Machine (SVM) algorithm and ResNet50, a pre-trained Convolutional Neural Network (CNN), as a feature extractor from digital images of tree bark. The approach of using pre-trained networks is known as Transfer Learning. The model predictions follow these steps:
- **1 - Resizing**: High-resolution images are resized by 20%;
- **2 - Patches Extraction**: 50 patches of size 224 x 224 are randomly extracted from each original image;
- **3 - Pre-processing**: Applies the pre-processing steps defined by the pre-trained ResNet50 network to the 50 patches;
- **4 - Feature Extraction**: Utilizes the ResNet50 model with ImageNet weights and all convolutional layers frozen to extract features from the 50 patches; and
- **5 - Classification**: Employs a classifier trained on the **“Amazon Bark”** dataset to predict the class probability for each patche. A majority vote strategy, based on the sum of maximum class probabilities, is then applied to estimate the highest average class probability. Note that the classifier is currently configured to predict up to 16 classes. Future efforts will focus on expanding the image collection, including new species, to enhance specimen representativeness. This expansion will account for various factors influencing bark variations across tree species.