# Make a flask API for our DL Model
import werkzeug
# This next lime Prevents ImportErrors - flask-restplus currently gets broken by 
# Werkzeug 1.0.0. Alternatively, you could also downgrade werkzeug 
# (the package Python uses to interface with an HTTP web server)
# Note: line 6 must happen BEFORE you import Flask to be able to work!
werkzeug.cached_property = werkzeug.utils.cached_property

# import for time objects
import datetime as dt 

# import for Firebase services
import firebase_admin
from firebase_admin import credentials, firestore

from tensorflow import keras
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from flask_restplus import Api, Resource, fields
from flask import Flask, request, jsonify
import numpy as np
from werkzeug.datastructures import FileStorage
from PIL import Image
from keras.models import model_from_json
import tensorflow as tf

# init the Firebase SDK
cred = credentials.Certificate(
    'ds23-hw2-1d580-firebase-adminsdk-8gqfi-f436991c85.json')
firebase_app = firebase_admin.initialize_app(cred)
# init Cloud Firestore
db = firestore.client()

application = app = Flask(__name__)
api = Api(app, version='1.0', title='MNIST Classification', description='CNN for Mnist')
ns = api.namespace('Make_School', description='Methods')

single_parser = api.parser()  # parsing args is one of the benefits of Flask-RESTPlus
single_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

"""
model = load_model('model_weights.h5')  # 
graph = tf.get_default_graph()  # good to add
"""

# Model reconstruction from JSON file - do this only once!
# not in the body of a function
with open('model_architecture.json', 'r') as f:
    model = model_from_json(f.read())

# Load weights into the new model
model.load_weights('model_weights.h5')
graph = tf.get_default_graph()  # good to add


@ns.route('/prediction')
class CNNPrediction(Resource):
    """Uploads your data to the CNN"""
    @api.doc(parser=single_parser, description='Upload an mnist image')
    def post(self):
        args = single_parser.parse_args()
        image_file = args.file  # reading args from file
        image_file.save('posted_img.png')  # save the file
        img = Image.open('posted_img.png')  # open the image
        image_red = img.resize((28, 28))  # reshape for the model dimension requirements
        image = img_to_array(image_red)
        print(image.shape)
        x = image.reshape(1, 28, 28, 1)  # 1 image of 28x28 pixels, 1 channel (grayscale)
        x = x/255  # data normalization
        # This is not good, because this code implies that the model will be
        # loaded each and every time a new request comes in.
        # model = load_model('my_model.h5')
        
        # PREDICTION! 
        with graph.as_default():
            out = model.predict(x)
        print(out[0])
        print(np.argmax(out[0]))
        r = str(np.argmax(out[0]))

        # write to the Cloudstore instance db
        date = str(dt.datetime.now())
        data = {
            u'date': date,
            u'file_name': u'posted_img.png',
            u'result': r  # represents the prediction of model
        }
        # Add a new doc in collection 'Predictions' with date as the ID
        db.collection(u'predictions').document(date).set(data)

        # return the classification
        return {'prediction': r}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
