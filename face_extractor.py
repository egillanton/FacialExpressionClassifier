import os
import sys
import cv2
import matplotlib.pyplot as plt


def rotate(image, deg):
    rows, cols, _ = image.shape
    M = cv2.getRotationMatrix2D((cols/2, rows/2), -deg, 1)
    dst = cv2.warpAffine(image, M, (cols, rows))
    return dst

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

img = cv2.resize(optFace, (image_size, image_size))
flipped_image = cv2.flip(img, 1)
# Clockwise
clockwise_rot5_image = rotate(img, 5)
# Antin Clockwise
anticlockwise_rot5_image = rotate(img, -5)

plt.title("Detected Face")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

plt.title("Horizontal Flipped")
plt.imshow(cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB))
plt.show()

plt.title("Clockwise Rotated 5° Degrees")
plt.imshow(cv2.cvtColor(clockwise_rot5_image, cv2.COLOR_BGR2RGB))
plt.show()

plt.title("Anticlockwise Rotated 5° Degrees")
plt.imshow(cv2.cvtColor(anticlockwise_rot5_image, cv2.COLOR_BGR2RGB))
plt.show()