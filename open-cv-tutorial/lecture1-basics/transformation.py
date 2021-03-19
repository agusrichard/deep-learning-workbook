import os
import cv2 as cv
import numpy as np


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

photos_path = os.path.join(BASE_DIR, 'photos')
videos_path = os.path.join(BASE_DIR, 'videos')

img = cv.imread(os.path.join('photos', 'cats.jpg'))
cv.imshow('cats', img)

# Translation
def translate(img, x, y):
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translation_matrix, dimensions)

translated = translate(img, 100, 100)
cv.imshow('translated', translated)

# Rotation
def rotate(img, angle, center=None):
    (height, width) = img.shape[:2]

    if center == None:
        center = (width//2, height//2)
    
    rotation_matrix = cv.getRotationMatrix2D(center, angle, scale=1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotation_matrix, dimensions)

rotated = rotate(img, 90)
cv.imshow('rotated', rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)