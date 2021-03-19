import os
import cv2 as cv
import numpy as np

DIR = os.path.dirname(os.path.abspath(__file__))
people = [f for f in os.listdir(os.path.join(DIR, 'faces'))]
print(people)
haar_cascade = cv.CascadeClassifier(os.path.join(DIR, 'haar_face.xml'))

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(os.path.join(DIR, 'face_trained.yml'))

img = cv.imread(os.path.join(DIR, 'faces', 'Ben Afflek', '5.jpg'))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 3)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)