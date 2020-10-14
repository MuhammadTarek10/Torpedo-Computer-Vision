'''
Import here most important libraries
'''
import numpy as np
import cv2


def zero_channel(image, channel):
    '''
        Return image **excluding** the rgb channel specified
        Args:
            image: numpy array of shape(image_height, image_width, 3)
            channel: number specifying the channel (0 for B, 1 for G, 2 for R)
        Returns:
            out: numpy array of shape(image_height, image_width, 3)
    '''
    copied_image = np.copy(image)
    copied_image[:, :, channel] = np.zeros([image.shape[0], image.shape[1]])
    return copied_image

def draw_solid_square_slow(image, x, y, l, color):
    """ Returns image after drawing a square on the image using python nested loops
    Args:
        image: numpy array of shape(image_height, image_width, 3)
        (x,y): a tuple specifying upper left corner
        l: square edge length
        color: a tuple specifying (B,G,R)
    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """
    copied_image = np.copy(image)
    color_array = color
    '''
    # Nested Loops but a whole square
    for i in range(x, x + l):
        for j in range(y, y + l):
            copied_image[i][j] = color_array
    '''
    # Sqaure edges but not nested
    for i in range(y, y + l):
        copied_image[x][i] = color_array
    for j in range(x, x + l):
        copied_image[j][y] = color_array
    for i in range(y, y + l):
        copied_image[x + l - 1][i] = color_array
    for j in range(x, x + l):
        copied_image[j][y + l - 1] = color_array
    return copied_image


def draw_solid_square_fast(image, x, y, l, color):
    """ 
    Returns image after drawing a square on the image using numpy arrays operations
        Args:
            image: numpy array of shape(image_height, image_width, 3)
            (x,y): a tuple specifying upper left corner
            l: square edge length
            color: a tuple specifying (B,G,R)
        Returns:
            out: numpy array of shape(image_height, image_width, 3)
    """
    copied_image = np.copy(image)
    color_array = np.array(color)
    copied_image[x : x + l][y : y + l] = color_array
    return copied_image

def combine_images_h(img1, img2):
    """ 
    Return 2 images combined horizontally. If the heights of images are different, you
    may set additional space to black
        Args:
            img1: numpy array of shape(image_height, image_width, 3)
            img2: numpy array of shape(image_height, image_width, 3)
        Returns:
            out: numpy array
    """
    result = []
    copied_img1 = np.copy(img1)
    copied_img2 = np.copy(img2)
    if copied_img1.shape == copied_img2.shape:
        result = np.hstack((copied_img1, copied_img2))
    else:
        if copied_img1.shape[0] > copied_img2.shape[0]:
            filler = np.zeros(((copied_img1.shape[0] - copied_img2.shape[0]), copied_img2.shape[1], 3), dtype=np.uint8)
            add = np.vstack((copied_img2, filler))
            result = np.hstack((copied_img1, add))
        else:
            filler = np.zeros(((copied_img2.shape[0] - copied_img1.shape[0]), copied_img1.shape[1], 3), dtype=np.uint8)
            add = np.vstack((copied_img1, filler))
            result = np.hstack((copied_img2, add))
    return result


def combine_images_v(img1, img2):
    """ 
    Return 2 images combined vetically. If the widths of images are different, you
    may set additional space to black
        Args:
            img1: numpy array of shape(image_height, image_width, 3)
            img2: numpy array of shape(image_height, image_width, 3)
        Returns:
            out: numpy array
    """
    result = []
    copied_img1 = np.copy(img1)
    copied_img2 = np.copy(img2)
    if copied_img1.shape == copied_img2.shape:
        result = np.vstack((copied_img1, copied_img2))
    else:
        if copied_img1.shape[1] > copied_img2.shape[1]:
            filler = np.zeros((copied_img2.shape[0], (copied_img1.shape[1] - copied_img2.shape[1]), 3), dtype=np.uint8)
            add = np.hstack((copied_img2, filler))
            result = np.vstack((copied_img1, add))
        else:
            filler = np.zeros((copied_img1.shape[0], (copied_img2.shape[1] - copied_img1.shape[1]), 3), dtype=np.uint8)
            add = np.hstack((copied_img1, filler))
            result = np.vstack((copied_img2, add))
    return result


def my_bgr2gray(image):
    """
    Returns a grayscale image where each pixel value = (B+G+R)/3
        Args:
            image: numpy array of shape(image_height, image_width, 3)
        Returns:
            out: numpy array of shape(image_height, image_width, 3)
    """
    copied_image = np.copy(image)
    gray = np.zeros((image.shape[0], image.shape[1]), np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            gray[i, j] = np.clip(sum(image[i, j]) // 3, 0, 255)
    return gray


def normalize_img(image):
    """
    normalize each channel independently according to the following formula
    pixel = (channel_value - channel_mean)/channel_std
        Args:
            image: numpy array of shape(image_height, image_width, 3)
        Returns:
            out: numpy array of shape(image_height, image_width, 3)
    """
    copied_image = np.copy(image)
    result = np.zeros((image.shape[0], image.shape[1]), np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            mean = np.mean(copied_image[i, j])
            std = np.std(copied_image[i, j])
            value = sum(copied_image[i, j])
            if std == 0:
                result[i, j] = 0
                continue
            pixel = np.array((value - mean) // std)
            result[i, j] = pixel
    return result