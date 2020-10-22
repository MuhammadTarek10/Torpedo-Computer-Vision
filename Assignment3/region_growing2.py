import cv2
import numpy as np
from queue import Queue

def region_grow(img, x, y, threshold):
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    height, width = img.shape
    out = np.zeros((height, width, 1), np.uint8)
    region_size = 1
    difference = 0
    points = {}
    points[x, y] = img[x, y]
    img_size = height * width
    while difference < threshold and region_size < img_size:
        for i in range(len(neighbors)):
            if difference < threshold and region_size < img_size:
                xx = x + neighbors[i][0]
                yy = y + neighbors[i][1]
                check = xx < height and yy < width and xx >= 0 and yy >= 0
                if check:
                    if out[xx, yy] == 0:
                        points[xx, yy] = img[xx, yy]
                        print(x, y)
                        print(img[xx, yy])
                        out[xx, yy] = 255
                        region_size += 1
                difference = abs(img[xx, yy] - img[x, y])


    for key, value in points.items():
        out[key] = value
        print(out)
    return out