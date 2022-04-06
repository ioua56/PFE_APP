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

class Model2Classification:
    modality="ct"
    def configure(self):
        self.model = load_model('tumor_prediction.h5') 
        self.model.summary()
        self.size=(224,224)
        print("--------------------------------------Configuration Done-------------------------------------------")
            

    def run(self,data):
        if data.Modality!=self.modality:
            return 'Wrong modality for this model the correct modality is '+self.modality
        #get the picture resize it apply préprocessing to it and get through     

        shape = data.pixel_array.shape
        image_2d = data.pixel_array.astype(float)
        image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0
        image_2d_scaled = np.uint8(image_2d_scaled)
        with open("tmp.png", 'wb') as png_file:
            w = png.Writer(shape[1], shape[0], greyscale=True)
            w.write(png_file, image_2d_scaled)
        imageDicom = Image.open("tmp.png")
        t = imageDicom.resize(self.size)
        x = image.img_to_array(t)
        x = np.expand_dims(x,axis=0)
        img_data = preprocess_input(x)
        rs = self.model.predict(img_data)
        
        #00 musure la non tumeur 01 mesure la verite  du tumeur de 0 a 1
        
        if rs[0][0] >=0.5 :
            prediction = 'This image is NOT tumorous. from model 2'
        else:
            prediction = 'Warning! This image IS tumorous. from model 2'
        
        
        return prediction

repo = Repository()
repo.register('classification2', Model2Classification())  
