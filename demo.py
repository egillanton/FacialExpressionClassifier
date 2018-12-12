import os
import sys
# Remove Keras Debug Info
stdout = sys.stdout
sys.stdout =  open(os.devnull, 'w')
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import cv2
import numpy as np
import skimage 
from skimage.transform import resize
from keras.models import load_model
from skimage import data, io
from matplotlib import pyplot as plt


image_size = 128

class FaceExtractor():
    
    faceCascade = None
    

    def __init__(self, cascadePath):
        self.faceCascade = cv2.CascadeClassifier(cascadePath)
        
        
    def getFace(self, imagePath):
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(100, 100)
        )
        optFace = None
        
        if len(faces) < 1:
            optFace = image

        elif len(faces) >= 1:
            (x, y, w, h) = faces[0]
            for (x1, y1, w1, h1) in faces:
                a_opt = w * h
                a_face = w1 * h1
                if a_opt < a_face:
                    (x, y, w, h) = (x1, y1, w1, h1)

            optFace = image[y:y+h, x:x+w]
        
        retImage = cv2.resize(optFace, (image_size, image_size))
        return retImage

def PrintResults(results):
    values = results[0]
    lable_classes = ['Angry', 'Contemptuous', 'Disgusted', 'Fearful', 'Happy', 'Neutral', 'Sad', 'Surprised']

    width = 28
    print('-'*width)
    print('|' + ' '*5 + 'Class'  + ' '*5+ '| Score')
    print('-'*width)
    for i in values.argsort()[::-1]:
        print(f'| {lable_classes[i]}' + ' '* (14-len(lable_classes[i])) + f'| {values[i]*100:>.2f}%')
        print('-'*width)


def main():
    sys.stdout = stdout
    sys.stderr = stderr
    faceCrop = FaceExtractor('./utils/haarcascade_frontalface_default.xml')

    print('Loading Model...')
    model = load_model('./models/alexnet.h5')
    X =np.array([faceCrop.getFace(sys.argv[1]),])
    results =  model.predict(X)
    PrintResults(results)

main()