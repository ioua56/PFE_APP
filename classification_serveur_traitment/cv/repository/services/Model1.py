import base64
import numpy as np 
import png
import tensorflow as tf
import keras
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from PIL import Image
from tensorflow.keras.models import load_model
import pandas as pd 
import os
import warnings
warnings.filterwarnings("ignore")
from cv.repository.repository import Repository
from tensorflow.keras.preprocessing import image

class Model1Classification:
    modality="ct"
    def configure(self):
        self.model = load_model('tumor_prediction.h5') 
        self.model.summary()
        self.size=(224,224)
        print("--------------------------------------Configuration Done-------------------------------------------")
            

    def run(self,data):
        
        t = data.resize(self.size)
        x = image.img_to_array(t)
        x = np.expand_dims(x,axis=0)
        img_data = preprocess_input(x)
        rs = self.model.predict(img_data)
        
        #00 musure la non tumeur 01 mesure la verite  du tumeur de 0 a 1
        
        if rs[0][0] >=0.5 :
            prediction = 'This image is NOT tumorous. from model 1'
        else:
            prediction = 'Warning! This image IS tumorous. from model 1'
        
        print(prediction)
        return {'hello': prediction}

repo = Repository()
repo.register('classification1', Model1Classification())  
