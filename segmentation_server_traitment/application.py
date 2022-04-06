from crypt import methods
from email.policy import HTTP
from http.client import HTTPResponse
from flask import Flask, render_template, request, jsonify
from PIL import Image
import base64
import json
import pickle
from cv.pipeline import Pipeline, Repository, discover_services
from os import curdir
from os.path import join as pjoin
import os
import pydicom
# Eureka client regestyration
import py_eureka_client.eureka_client as eureka_client


# Eureka client regestration
eureka_client.init(eureka_server="http://localhost:8721/eureka",
                  app_name="segmentation_server_traitment",
                  instance_port=5002,
                  instance_host="localhost")



def im2json(im):
    """Convert a Numpy array to JSON string"""
    imdata = pickle.dumps(im)
    jstr = json.dumps({"image": base64.b64encode(imdata).decode('ascii')})
    return jstr

def json2im(jstr):
    """Convert a JSON string back to a Numpy array"""
    load = json.loads(jstr)
    imdata = base64.b64decode(load['image'])
    im = pickle.loads(imdata)
    return im    
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    
    return '<h1>bonjour , this is traitment server for tumor segmentation:)</h1> '

#----------------------------Main Function-----------------------------------------|
@app.route('/segmentation', methods=['POST'])                                     #| 
def segmentation():                                                               #|
                                                                                  #|
    dicomFile=request.json['dicomFile']                                           #|
    modelName=request.json['modelName']                                           #|
    modality=request.json['modality']                                             #|
    image=json2im(dicomFile)                                                      #|
                                                                                  #| 
    #getServices                                                                  #|-------------------------------------------------------------------------------------  
    discover_services()                                                           #|
    repository = Repository()                                                     #|
    instance = repository.get_service(modelName)                                  #|  
    instance.configure()                                                          #|
    pic=instance.run(image,modality)                                              #|
    pic_json=im2json(pic)                                                         #|
    return jsonify(pic_json)                                                      #|
                                                                                  #|                   
#----------------------------------------------------------------------------------|

#Ading a new model + his configuration------------------------------------------------------
@app.route('/add', methods=['POST'])
def add():
    
    data=request.files
    fileConfiguration=data['file']
    fileConfiguration.save(os.path.join("cv/repository/services/"+fileConfiguration.filename))

    modelWeights=data['model']
    modelWeights.save(os.path.join(""+modelWeights.filename))
    print("recieved and saving")
    return '<h1>model recievd </h1>'
#--------------------------------------------------------------------------------------------



@app.route('/services', methods=['GET'])
def services():
    discover_services()
    repository = Repository()
    #return repository.available_services()
    context=repository.available_services()
    context2=repository.available_services_html()
    print(context)
    print(context2)
    model_dictionary = dict(zip(context, context2))
    print(model_dictionary)
    return model_dictionary


#Not working yet -----------------------------------------------------------------------------------
@app.route('/remove_model', methods=['POST'])
def remove_Model():
    data=request.files
    print(data)
    #get the name of the model
    #change cwd to services
    #remove the specificated service 
    
    return "<h1>model removed</h1>"    
#-----------------------------------------------------------------------------------------------------    
""""
@app.route('/diagnostiquedicom', methods=['POST'])
def diagnostique():
    
    #i can add another parametre to specify if it is a classification or a segmentation .
    data=request.json
    image=data['image']
    model_name=data['modelname']
    
   
    #so we can acces directly to the request
    discover_services()
    
    repository = Repository()
    instance = repository.get_service(model_name)
    
    picture=json2im(image)
    instance.configure()
    return instance.run(picture) 
    """   

if __name__ == '__main__':
    app.run(debug=True, port=5002)