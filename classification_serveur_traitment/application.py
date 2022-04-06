from email.policy import HTTP
from http.client import HTTPResponse
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
#from PIL import Image
import base64
import json
import pickle

#from matplotlib.pyplot import spring
from cv.pipeline import Pipeline, Repository, discover_services
from os import curdir
from os.path import join as pjoin
import os
import pydicom
import re 
import base64
from base64 import b64decode
from io import BytesIO
from PIL import Image
# Eureka client regestyration
import py_eureka_client.eureka_client as eureka_client


# Eureka client regestration
eureka_client.init(eureka_server="http://localhost:8721/eureka",
                  app_name="classification_serveur_traitment",
                  instance_port=5001,
                  instance_host="localhost")

app = Flask(__name__)

# enable CORS
CORS(app)
def json2im(jstr):
    """Convert a JSON string back to a Numpy array"""
    load = json.loads(jstr)
    imdata = base64.b64decode(load['image'])
    im = pickle.loads(imdata)
    return im

@app.route('/', methods=['GET'])
def index():
    
    #data = request.files['image']
    #print(data)
    return '<h1>bonjour , this is traitment server for tumor classification :)</h1> '

"""
@app.route('/diagnostique', methods=['POST'])
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

#----------------------------Main Function-----------------------------------------|
@app.route('/classification', methods=['POST'])                                   #| 
def classify():                                                                   #| 
    dicomFile=request.json['dicomFile']                                           #|
    modelName=request.json['modelName']                                           #|
    dicomFile=pydicom.dataset.Dataset.from_json(dicomFile)                        #| 
    #getServices                                                                  #|-------------------------------------------------------------------------------------  
    discover_services()                                                           #|
    repository = Repository()                                                     #|
    instance = repository.get_service(modelName)                                  #|  
    instance.configure()                                                          #|
    return instance.run(dicomFile)                                                #|
#----------------------------------------------------------------------------------|

#-------------------------------Add Model-----------------------------------|
@app.route('/add', methods=['POST'])
def add():
    
    data=request.files
    fileConfiguration=data['file']
    fileConfiguration.save(os.path.join("cv/repository/services/"+fileConfiguration.filename))

    modelWeights=data['model']
    modelWeights.save(os.path.join(""+modelWeights.filename))
   
    #filename=data['filename']
    print("recieved and saving")
    return '<h1>model recievd </h1>' 
#----------------------------------------------------------------------------------|

#----------------------------------------------------------------------------------|
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
    spring_object=[]
    for key, value in model_dictionary.items():
        tmp_dict={'value':value,'label':key}
        spring_object.append(tmp_dict)
    
    
       
        

# parse x:
        print("spring_object")
        print(spring_object)

    print(model_dictionary)
    #return spring_object
    return jsonify(spring_object)
#----------------------------------------------------------------------------------|
@app.route('/remove_model', methods=['POST'])
def remove_Model():
    data=request.files
    print(data)
    #get the name of the model
    #change cwd to services
    #remove the specificated service 
    
    return "<h1>model removed</h1>"    
#----------------------test---------------------------------
@app.route('/classificationendpoint', methods=['POST'])                                   #| 
def classify2(): 
    image = request.form['image']
    try:
        modelName = request.form['modelName']
    except:
        modelName='Model1Classification'   
    
    image = re.sub("^data:image/png;base64,", "", image)
    image = b64decode(image)
    image = BytesIO(image)
    #im = Image.open(image)  
    im=Image.open(image).convert('RGB')

    #getServices 
    # -----------------------------------------------------------------------------| 
    discover_services()                                                           #|
    repository = Repository()                                                     #|
    instance = repository.get_service(modelName)                                  #|  
    instance.configure()                                                          #|
    return instance.run(im)                                                       #|
#----------------------------------------------------------------------------------|
  

if __name__ == '__main__':
    app.run(debug=True,port=5001)
