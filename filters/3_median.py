import random
import cv2
import numpy as np


def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output
 
image = cv2.imread('angio.tif',0)

cv2.imshow('Original', image)

# Add salt and pepper noise to image
image_sp = sp_noise(image, 0.05)

cv2.imshow('Image S&P', image_sp)

# Apply average kernel
kernel_avg = np.ones((3,3))
kernel_avg = kernel_avg / kernel_avg.sum()
 
average = cv2.filter2D(src=image_sp, ddepth=-1, kernel=kernel_avg)

cv2.imshow('Average', average)

# Apply median kernel
median = cv2.medianBlur(src=image_sp, ksize=5)

cv2.imshow('Median', median)
cv2.waitKey(0)