import os
import cv2 as cv
import numpy as np

DIR = os.path.dirname(os.path.abspath(__file__))

people = [f for f in os.listdir(os.path.join(DIR, 'faces'))]

haar_cascade = cv.CascadeClassifier(os.path.join(DIR, 'haar_face.xml'))

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, 'faces', person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            if img_array is None:
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, w:w+h]
                features.append(faces_roi)
                labels.append(label)


create_train()
print('Training done ---------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)