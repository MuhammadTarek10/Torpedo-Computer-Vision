import matplotlib.pyplot as plt
import numpy as np
import cv2
from Assignment1 import *
plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['image.cmap'] = 'gray'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cropped_box = frame[:400, :400]
    blue_upper_left = draw_solid_square_slow(frame, 0, 0, 20, (255, 0, 0))
    red_upper_right = draw_solid_square_slow(frame, 0, frame.shape[1] - 20, 20, (0, 0, 255))
    cv2.imshow("Video", frame)
    cv2.imshow("Cropped", cropped_box)
    cv2.imshow("Blue square", blue_upper_left)
    cv2.imshow("Red square", red_upper_right)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()