# Lecture 1 -- Basics

## Read Images and Videos
- cv.imread() -> read images
- cv.imshow() -> show images
- cv.waitKey() -> wait for key to be pressed
- cv.VideoCapture will return video frame by frame. You can show frame by frame using forloop.
- If you want to use videocam give argument = 0 to the first positional argument to VideoCapture

## Rescale and Resize
-  cv.resize(frame, dimensions, interpolation)
-  capture.set(3, width) -> chaging resolution of live video
-  capture.set(4, height) -> changin resolution of live video