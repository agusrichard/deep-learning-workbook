import os
import cv2 as cv
import numpy as np  

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

photos_path = os.path.join(BASE_DIR, 'photos')
videos_path = os.path.join(BASE_DIR, 'videos')

img = cv.imread(os.path.join(photos_path, 'cats.jpg'))
cv.imshow('cats', img)

height = img.shape[0]
width = img.shape[1]

blank = np.zeros(shape=(height, width), dtype='uint8')
cv.imshow('blank', blank)

rectangle = cv.rectangle(blank.copy(), (width//4, height//4), ((width//4)*3, (height//4)*3), 255, -1)
circle = cv.circle(blank.copy(), (width//2, height//2), 150, 255, -1)
cv.imshow('rectangle', rectangle)

print('rectangle shpae', rectangle.shape)

cropped_circle = cv.bitwise_and(img, img, mask=circle)
cv.imshow('cropped_circle', cropped_circle)

cv.waitKey(0)