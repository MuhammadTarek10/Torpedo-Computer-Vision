from Assignment1 import *

'''
# Zero Channel Function
# Reading image
img = cv2.imread("Boku.jpg")
# Removing color channel (BLUE_CHANNEL = 0, GREEN_CHANNEL = 1, RED_CHANNEL = 2)
# Removing Blue for example
no_blue = zero_channel(img, 0)
# Saving the result in another jpg
cv2.imwrite("No Blue.jpg", no_blue)
# Showing the result
cv2.imshow("zero_channel_function", no_blue)
cv2.imshow("original", img)
cv2.waitKey(0)
'''

'''
# Draw a sqaure using loops (Slow)
# Reading image
img = cv2.imread("Boku.jpg")
# Defining parameters
x = 0
y = 0
l = img.shape[1]
color = (200, 55, 200) # BGR
# Draw a square
square = draw_solid_square_slow(img, x, y, l, color)
# Showing the result
cv2.imshow("draw_solid_square_slow_function", square)
cv2.waitKey(0)
'''

'''
# Draw a sqaure using numpy operations (fast)
# Reading image
img = cv2.imread("Boku.jpg")
# Defining parameters
x = 0
y = 0
l = img.shape[1]
color = (200, 55, 200) # BGR
# Draw a square
square = draw_solid_square_fast(img, x, y, l, color)
# Showing the result
cv2.imshow("draw_solid_square_fast_function", square)
cv2.waitKey(0)
'''

'''
# Combine images Horizantly
# Reading images
img1 = cv2.imread("Boku.jpg")
img2 = cv2.imread("Sasuke.jpg")
# Trying same image
#h_img_same = combine_images_h(img1, img1)
# Trying different images
h_img_different = combine_images_h(img1, img2)
# Showing results
#cv2.imshow("combine_images_h(Same)", h_img_same)
cv2.imshow("combine_images_h(Different)", h_img_different)
cv2.waitKey(0)
'''

'''
# Combine images Vertically
# Reading images
img1 = cv2.imread("Boku.jpg")
img2 = cv2.imread("Sasuke.jpg")
# Trying same image
#v_img_same = combine_images_v(img1, img1)
# Trying different images
v_img_different = combine_images_v(img1, img2)
# Showing results
#cv2.imshow("combine_images_v(Same)", v_img_same)
cv2.imshow("combine_images_v(Different)", v_img_different)
cv2.waitKey(0)
'''

'''
# BGR to Gray
# Reading image
img = cv2.imread("Boku.jpg")
# Turining to gray
gray = my_bgr2gray(img)
cv2.imshow("my_bgr2gray", gray)
cv2.waitKey(0)
'''

'''
# Normalize Image
# Reading image
img = cv2.imread("Boku.jpg")
# normalizing
normalized_img = normalize_img(img)
cv2.imshow("normalize_img_function", normalized_img)
cv2.waitKey(0)
'''

#cv2.destroyAllWindows()
