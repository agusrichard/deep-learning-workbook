import cv2 as cv

# Read and show image to the screen
# img = cv.imread('photos/cat1.jpg')
# cv.imshow('cat', img)
# cv.waitKey(0)

# Read and play video
capture = cv.VideoCapture('videos/kitten.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Kitten Videos', frame)

    if cv.waitKey(20) & 0xff == ord('d'):
        break

capture.release()
cv.destroyAllWindows()