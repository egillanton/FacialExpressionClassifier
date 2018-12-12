import os
import random
import cv2
import numpy as np
import json


from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, BatchNormalization, Dropout, Activation
from keras.optimizers import SGD, Adam
from sklearn.metrics import classification_report

import matplotlib.pyplot as plt

random_seed = 42   # include for reproducability
random.seed(random_seed)

path = './data/'
image_size = 128
batch_size = 8

#custom sequence generator
from skimage.io import imread
from skimage.transform import resize
from keras.utils import Sequence


if not './angry' in os.listdir(path):
    for file in os.listdir(path):
        if '.jpg' in file and not file.startswith('.'):
           # Assuming all jpg files are of RaFD format
            img_properties = file.split('_')
            label = img_properties[-2]

            # Create directory for label (if it doesn't exist)
            if not os.path.isdir(os.path.join(path, label)):
                os.mkdir(os.path.join(path, label))

            # Move file to label directory
            os.rename(os.path.join(path, file), os.path.join(path, label, file))
        
    print('Successfully unpacked images into folders')