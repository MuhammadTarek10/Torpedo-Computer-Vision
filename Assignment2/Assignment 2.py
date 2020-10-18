
import cv2 as cv
import numpy as np
from colors import *


cap = cv.VideoCapture(0)


while True:
    _, img = cap.read()
    if cv.waitKey(1) == ord('y'):
        result = yellow_track(img)
    elif cv.waitKey(1) == ord('n'):
        result = normal(img)
    elif cv.waitKey(1) == ord('b'):
        result = blue_track(img)
    elif cv.waitKey(1) == ord('g'):
        result = green_track(img)
    elif cv.waitKey(1) == ord('o'):
        result = orange_track(img)
    elif cv.waitKey(1) == ord('q'):
        break
    else:
        result = normal(img)
    cv.imshow("window", result)
        
   


