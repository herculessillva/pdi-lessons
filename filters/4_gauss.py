import random
import cv2
import numpy as np


def gauss_noise(image):
    '''
    Add gaussian noise to image
    '''
    row,col= image.shape
    mean = 0
    var = 0.5
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col)).astype(np.uint8)
    print(gauss)
    gauss = gauss.reshape(row,col)
    output = image + gauss
    return output

 
image = cv2.imread('angio.tif',0)

cv2.imshow('Original', image)

# Add gaussian noise to image
image_gauss = gauss_noise(image)

cv2.imshow('Image Gauss', image_gauss)

# Apply average kernel

# Apply average kernel
kernel_avg = np.ones((3,3))
kernel_avg = kernel_avg / kernel_avg.sum()

average = cv2.filter2D(src=image_gauss, ddepth=-1, kernel=kernel_avg)

cv2.imshow('Average', average)

# Apply median kernel
kernel_gauss = np.array([[1, 2, 1],
                    [2, 4, 2],
                    [1, 2, 1]])
cv2.imshow('kernel_gauss', (255*kernel_gauss/kernel_gauss.max()).astype(np.uint8))
kernel_gauss = kernel_gauss / kernel_gauss.sum()
 
gaussian = cv2.filter2D(src=image_gauss, ddepth=-1, kernel=kernel_gauss)


cv2.imshow('Gaussian', gaussian)
cv2.waitKey(0)