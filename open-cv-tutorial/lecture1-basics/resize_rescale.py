import os
import cv2 as cv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

photos_path = os.path.join(BASE_DIR, 'photos')
videos_path = os.path.join(BASE_DIR, 'videos')

def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def change_resolution(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)

# image = cv.imread(os.path.join(photos_path, 'cat1.jpg'))

# rescaled_image = rescale_frame(image, 0.3)
# cv.imshow('cat', rescaled_image)

# cv.waitKey(0)

capture = cv.VideoCapture(os.path.join(videos_path, 'kitten.mp4'))

while True:
    isTrue, frame = capture.read()
    rescaled_frame = rescale_frame(frame, scale=0.5)
    cv.imshow('Kitten Videos', rescaled_frame)

    if cv.waitKey(20) & 0xff == ord('d'):
        break

capture.release()
cv.destroyAllWindows()