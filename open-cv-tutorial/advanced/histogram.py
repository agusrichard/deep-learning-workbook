import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

photos_path = os.path.join(BASE_DIR, 'photos')
videos_path = os.path.join(BASE_DIR, 'videos')

img = cv.imread(os.path.join(photos_path, 'cats.jpg'))
cv.imshow('cats', img)

height = img.shape[0]
width = img.shape[1]

blank = np.zeros(shape=(height, width), dtype='uint8')
circle = cv.circle(blank.copy(), (width//2, height//2), 150, 255, -1)

masked_img = cv.bitwise_and(img, img, mask=circle)
cv.imshow('masked_img', masked_img)

img_hist = cv.calcHist([img], [0], circle, [256], [0, 256])
print(img_hist.shape)

plt.figure()
plt.title('Image Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(img_hist)
plt.xlim([0,256])

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])


plt.show()


cv.waitKey(0)