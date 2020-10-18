import cv2 as cv
import numpy as np







def empty(a):
    pass

cv.namedWindow("Bars")
cv.resizeWindow("Bars", 640, 240)
cv.createTrackbar("Hue Min", "Bars", 0, 179, empty)
cv.createTrackbar("Hue Max", "Bars", 179, 179, empty)
cv.createTrackbar("Sat Min", "Bars", 0, 255, empty)
cv.createTrackbar("Sat Max", "Bars", 255, 255, empty)
cv.createTrackbar("Val Min", "Bars", 0, 255, empty)
cv.createTrackbar("Val Max", "Bars", 255, 255, empty)


def normal(img):
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min", "Bars")
    h_max = cv.getTrackbarPos("Hue Max", "Bars")
    s_min = cv.getTrackbarPos("Sat Min", "Bars")
    s_max = cv.getTrackbarPos("Sat Max", "Bars")
    v_min = cv.getTrackbarPos("Val Min", "Bars")
    v_max = cv.getTrackbarPos("Val Max", "Bars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    mins = np.array([h_min, s_min, v_min])
    maxes = np.array([h_max, s_max, v_max])
    mask = cv.inRange(hsv_img, mins, maxes)
    result = cv.bitwise_and(img, img, mask=mask)
    return result

def yellow_track(img):
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.createTrackbar("Hue Min", "Bars", 0, 179, empty)
    cv.createTrackbar("Hue Max", "Bars", 49, 179, empty)
    cv.createTrackbar("Sat Min", "Bars", 212, 255, empty)
    cv.createTrackbar("Sat Max", "Bars", 255, 255, empty)
    cv.createTrackbar("Val Min", "Bars", 91, 255, empty)
    cv.createTrackbar("Val Max", "Bars", 255, 255, empty)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min", "Bars")
    h_max = cv.getTrackbarPos("Hue Max", "Bars")
    s_min = cv.getTrackbarPos("Sat Min", "Bars")
    s_max = cv.getTrackbarPos("Sat Max", "Bars")
    v_min = cv.getTrackbarPos("Val Min", "Bars")
    v_max = cv.getTrackbarPos("Val Max", "Bars")
    mins = np.array([h_min, s_min, v_min])
    maxes = np.array([h_max, s_max, v_max])
    mask = cv.inRange(hsv_img, mins, maxes)
    result = cv.bitwise_and(img, img, mask=mask)
    return result


def blue_track(img):
   hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
   cv.createTrackbar("Hue Min", "Bars", 99, 179, empty)
   cv.createTrackbar("Hue Max", "Bars", 125, 179, empty)
   cv.createTrackbar("Sat Min", "Bars", 94, 255, empty)
   cv.createTrackbar("Sat Max", "Bars", 255, 255, empty)
   cv.createTrackbar("Val Min", "Bars", 1, 255, empty)
   cv.createTrackbar("Val Max", "Bars", 255, 255, empty)
   hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
   h_min = cv.getTrackbarPos("Hue Min", "Bars")
   h_max = cv.getTrackbarPos("Hue Max", "Bars")
   s_min = cv.getTrackbarPos("Sat Min", "Bars")
   s_max = cv.getTrackbarPos("Sat Max", "Bars")
   v_min = cv.getTrackbarPos("Val Min", "Bars")
   v_max = cv.getTrackbarPos("Val Max", "Bars")
   mins = np.array([h_min, s_min, v_min])
   maxes = np.array([h_max, s_max, v_max])
   mask = cv.inRange(hsv_img, mins, maxes)
   result = cv.bitwise_and(img, img, mask=mask)
   return result


def green_track(img):
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.createTrackbar("Hue Min", "Bars", 40, 179, empty)
    cv.createTrackbar("Hue Max", "Bars", 91, 179, empty)
    cv.createTrackbar("Sat Min", "Bars", 172, 255, empty)
    cv.createTrackbar("Sat Max", "Bars", 255, 255, empty)
    cv.createTrackbar("Val Min", "Bars", 3, 255, empty)
    cv.createTrackbar("Val Max", "Bars", 79, 255, empty)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min", "Bars")
    h_max = cv.getTrackbarPos("Hue Max", "Bars")
    s_min = cv.getTrackbarPos("Sat Min", "Bars")
    s_max = cv.getTrackbarPos("Sat Max", "Bars")
    v_min = cv.getTrackbarPos("Val Min", "Bars")
    v_max = cv.getTrackbarPos("Val Max", "Bars")
    mins = np.array([h_min, s_min, v_min])
    maxes = np.array([h_max, s_max, v_max])
    mask = cv.inRange(hsv_img, mins, maxes)
    result = cv.bitwise_and(img, img, mask=mask)
    return result


def orange_track(img):
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.createTrackbar("Hue Min", "Bars", 13, 179, empty)
    cv.createTrackbar("Hue Max", "Bars", 22, 179, empty)
    cv.createTrackbar("Sat Min", "Bars", 66, 255, empty)
    cv.createTrackbar("Sat Max", "Bars", 255, 255, empty)
    cv.createTrackbar("Val Min", "Bars", 7, 255, empty)
    cv.createTrackbar("Val Max", "Bars", 85, 255, empty)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min", "Bars")
    h_max = cv.getTrackbarPos("Hue Max", "Bars")
    s_min = cv.getTrackbarPos("Sat Min", "Bars")
    s_max = cv.getTrackbarPos("Sat Max", "Bars")
    v_min = cv.getTrackbarPos("Val Min", "Bars")
    v_max = cv.getTrackbarPos("Val Max", "Bars")
    mins = np.array([h_min, s_min, v_min])
    maxes = np.array([h_max, s_max, v_max])
    mask = cv.inRange(hsv_img, mins, maxes)
    result = cv.bitwise_and(img, img, mask=mask)
    return result