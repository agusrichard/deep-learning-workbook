import os
import cv2 as cv
import numpy as np  

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

photos_path = os.path.join(BASE_DIR, 'photos')
videos_path = os.path.join(BASE_DIR, 'videos')

img = cv.imread(os.path.join(photos_path, 'lady.jpg'))
cv.imshow('Park', img)

blank = np.empty(shape=(img.shape[0], img.shape[1]), dtype='uint8')
cv.imshow('blank', blank)

b, g, r = cv.split(img)
cv.imshow('b', b)
cv.imshow('g', g)
cv.imshow('r', r)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


cv.waitKey(0)