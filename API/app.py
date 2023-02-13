#Import necessary libraries
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import os
from tensorflow import keras

#import packages
import pandas as pd       
import matplotlib as mat
import matplotlib.pyplot as plt    
import numpy as np
import seaborn as sns
import splitfolders
# %matplotlib inline





from PIL import Image
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

import numpy as np
from tensorflow.keras.preprocessing import image
# import warnings
# warnings.filterwarnings('ignore')

# color = sns.color_palette()
# %matplotlib inline
# %config InlineBackend.figure_format="png"


# Create flask instance 
# __name__ current file ie app.py
app = Flask(__name__, template_folder = 'templates')

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'tif']
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def init():
#     global graph
#     graph = tf.compat.v1.get_default_graph()

# IMG_SIZE = 224
# BATCH = 64
# SEED = 42





def read_image(filename):

    img = load_img(filename, target_size = (224,224))
    img =  img_to_array(img)
    img = img/255
    img = np.expand_dims(img, axis = 0)

    return img

# route decorator / means url asociated with the home page user visits app domain at given route, it will execute the home function.

@app.route("/", methods=['GET', 'POST'])
def home():

    return render_template('index.html')

@app.route("/predict", methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']


        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join('static/images', filename)
            file.save(file_path)
            img = read_image(file_path)

            # with graph.as_default():
            model1 = load_model('model00000200.h5')
            # model1.compile(loss='binary_crossentropy', optimizer = keras.optimizers.Adam(learning_rate=5e-5), metrics='binary_accuracy')
            result = model1.predict(img)
            # print(class_prediction)

            if result<0.5:
                product = "The image classified is Inflamed"
            else:
                product = "The image classified is NonInflamed"
            
            return render_template('predict.html', product = product, user_image = file_path)

    return render_template('predict.html')

if __name__ == "__main__":
    # init()
    app.run()