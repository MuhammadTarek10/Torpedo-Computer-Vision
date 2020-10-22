import numpy as np
import cv2


def global_automatic_threshold(img, threshold, mean1 = 0, mean2 = 0):
    height, width = img.shape
    mean1 = np.mean(img[:height//2, :width//2])
    mean2 = np.mean(img[height//2:, width//2:])
    threshold = 0.5 * (mean1 + mean2)
    while abs(mean1 - threshold) > 5 and abs(mean2 - threshold) > 5:
        threshold, mean1, mean2 = global_automatic_threshold(img/2, threshold, mean1, mean2)
    return threshold, mean1, mean2



img = cv2.imread("Boku.jpg", 0)
threshold = np.mean(img)
print("Threshold before is: {}".format(threshold))
out, mean1, mean2 = global_automatic_threshold(img, threshold)
print("Mean1 is: {}, Mean2 is: {}".format(mean1, mean2))
print("Threshold after is: {}".format(out))

