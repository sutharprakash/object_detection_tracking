#!/usr/bin/env python

import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from yolo_class import *

y1 = yoloDetect()
app = Flask(__name__)



def predict_(filename):
   name = y1.run(filename)
   return "http://192.168.2.157:4243/static/img/" + name + ".png"
    # return predict()

@app.route('/')
def upload_file():
   return render_template('upload.html')
    
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():

   if request.method == 'POST':

      print(request.files)
      f = request.files['file']
      f.filename = secure_filename(f.filename)
      f.filename = "./static/img/" + f.filename
      print(f.filename)
      f.save(f.filename)
      return predict_(f.filename)

@app.route('/hello', methods = ['GET', 'POST'])
def hello():
    return os.getcwd()
        
if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0', port=4243)
