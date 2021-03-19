import os
import cv2 as cv
import numpy as np


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

photos_path = os.path.join(BASE_DIR, 'photos')
videos_path = os.path.join(BASE_DIR, 'videos')

blank = np.empty(shape=(600, 800, 3), dtype='uint8')
cv.imshow('Blank Image', blank)

# 1. Paint the image a certain color
blank[100:400, 100:400, :] = [0, 0, 255]
cv.imshow('Painted', blank)

# 2. Draw Rectangle
cv.rectangle(blank, (200, 200), (400, 400), (122, 122, 122), thickness=-1)
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (200, 200), 50, (123, 231, 98), thickness=5)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0, 0), (300, 300), (213, 143, 65))
cv.imshow('Line', blank)

# 5. Write a text
cv.putText(blank, 'Sekardayu Hana Pradiani', (0, 300), cv.FONT_HERSHEY_TRIPLEX, 1.0, (201, 63, 93))
cv.imshow('Text', blank)

cv.waitKey(0)