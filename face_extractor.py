import os
import sys
import cv2
import matplotlib.pyplot as plt

image_size = 128
face_cascade = cv2.CascadeClassifier('./utils/haarcascade_frontalface_default.xml')

image = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
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

face_image = cv2.resize(optFace, (image_size, image_size))

plt.title("Detected Face")
plt.imshow(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB))
plt.show()