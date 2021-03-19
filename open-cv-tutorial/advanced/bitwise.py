import os
import cv2 as cv
import numpy as np  

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

photos_path = os.path.join(BASE_DIR, 'photos')
videos_path = os.path.join(BASE_DIR, 'videos')

img = cv.imread(os.path.join(photos_path, 'park.jpg'))
cv.imshow('park', img)

height = img.shape[0]
width = img.shape[1]

blank = np.zeros(shape=(height, width), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (width//4, height//4), ((width//4)*3, (height//4)*3), 255, -1)
circle = cv.circle(blank.copy(), (width//2, height//2), 150, 255, -1)
cv.imshow('rectangle', rectangle)
cv.imshow('cicle', circle)

bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise and', bitwise_and)

# bitwise OR --> non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Circle NOT', bitwise_not)

cv.waitKey(0)