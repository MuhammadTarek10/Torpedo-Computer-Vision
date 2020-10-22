from region_growing2 import *



def process_img(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        out = region_grow(img, x, y, 20)
        cv2.imshow('out', out)
        cv2.waitKey(0)
        cv2.destroyWindow('out')
        
clicked = False
cv2.namedWindow('input')
cv2.setMouseCallback('input', process_img)
img = cv2.imread('Boku.jpg', 0)
img = cv2.GaussianBlur(img, (5, 5), 1)
while True:
    cv2.imshow('input', img)

    if 0xFF & cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()