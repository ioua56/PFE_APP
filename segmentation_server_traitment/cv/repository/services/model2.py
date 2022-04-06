import json
import base64
import numpy as np 
import png
import tensorflow as tf
import keras
import numpy as np # linear algebra
import pandas as pd
from PIL import Image
import os
import matplotlib.pyplot as plt
import cv2
from tqdm import tqdm_notebook, tnrange
from glob import glob
from itertools import chain
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
from skimage.io import imread, imshow, concatenate_images
from skimage.transform import resize
from skimage.morphology import label
from sklearn.model_selection import train_test_split

import tensorflow as tf
from tensorflow import keras
from skimage.color import rgb2gray
from tensorflow.keras import Input
from tensorflow.keras.models import Model, load_model, save_model
from tensorflow.keras.layers import Input, Activation, BatchNormalization, Dropout, Lambda, Conv2D, Conv2DTranspose, MaxPooling2D, concatenate
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

from tensorflow.keras import backend as K
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
smooth=100
def dice_coef(y_true, y_pred):
    y_truef=K.flatten(y_true)
    y_predf=K.flatten(y_pred)
    And=K.sum(y_truef* y_predf)
    return((2* And + smooth) / (K.sum(y_truef) + K.sum(y_predf) + smooth))

def dice_coef_loss(y_true, y_pred):
    return -dice_coef(y_true, y_pred)

def iou(y_true, y_pred):
    intersection = K.sum(y_true * y_pred)
    sum_ = K.sum(y_true + y_pred)
    jac = (intersection + smooth) / (sum_ - intersection + smooth)
    return jac

def jac_distance(y_true, y_pred):
    y_truef=K.flatten(y_true)
    y_predf=K.flatten(y_pred)

    return - iou(y_true, y_pred)

class Model2Segmentation:
    modality="MR"
    def configure(self):
        self.model = load_model('unet_brain_mri_seg.hdf5', custom_objects={'dice_coef_loss': dice_coef_loss, 'iou': iou, 'dice_coef': dice_coef})
        #self.model = load_model('unet_brain_mri_seg.hdf5') 
        #self.model.summary()
        self.size=(256,256)
        print("--------------------------------------Configuration Done-------------------------------------------")
            

    def run(self,data, modality):
        if modality!=self.modality:
            return 'Wrong modality for this model the correct modality is '+self.modality
        
        #get the picture resize it apply préprocessing to it and get through     
        data.save('tmp.png')
        
        img = cv2.imread('tmp.png')
        img = cv2.resize(img ,self.size)
        img = img / 255
        img = img[np.newaxis, :, :, :]
        pred=self.model.predict(img)
        plt.figure(figsize=(12,12))
        plt.imshow(np.squeeze(pred) > .5)
        plt.title('Prediction')
        plt.ioff()
        plt.savefig('tomporaire_result.png')
        plt.close()
        im = Image.open("tomporaire_result.png") #i will send back this one but i need a more nice picutre     
        return im

repo = Repository()
repo.register('segmentation2', Model2Segmentation())  
