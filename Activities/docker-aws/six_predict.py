# Train, Evaluate and Save the DL Model

from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential, model_from_json
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import numpy as np
import tensorflow as tf

# Image Visualization
from matplotlib import image
import matplotlib.pyplot as plt
from PIL import Image


'''Get the model ready'''
with open('model_architecture.json', 'r') as f:
    model = model_from_json(f.read())
    # Load Weights
    model.load_weights('model_weights.h5')

# compile the model

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])


'''Predicting on Number 6'''
six_img = image.imread('img_35.jpg')
plt.imshow(six_img)
plt.show()

# passing into the model
six_img = six_img.astype('float32')
six_img /= 255
six_img = six_img.reshape(1, 28, 28, 1)
six_prediction = model.predict(six_img)
print(six_prediction[0])
print(np.argmax(six_prediction[0]))