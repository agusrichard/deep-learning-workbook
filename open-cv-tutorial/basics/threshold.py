import os
import cv2 as cv
import numpy as np


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

photos_path = os.path.join(BASE_DIR, 'photos')
videos_path = os.path.join(BASE_DIR, 'videos')

img = cv.imread(os.path.join('photos', 'cats.jpg'))
cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)