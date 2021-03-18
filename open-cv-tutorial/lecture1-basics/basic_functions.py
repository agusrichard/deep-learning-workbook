import os
import cv2 as cv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

photos_path = os.path.join(BASE_DIR, 'photos')
videos_path = os.path.join(BASE_DIR, 'videos')

img = cv.imread(os.path.join(photos_path, 'group 1.jpg'))
print(img.shape)
cv.imshow('Group 1', img)
cv.waitKey(0)