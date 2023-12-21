import cv2
import numpy as np
 
image = cv2.imread('angio.tif',0)

cv2.imshow('Original', image)

# Apply average kernel
kernel_avg = np.ones((25,25))
kernel_avg = kernel_avg / kernel_avg.sum()
cv2.imshow('kernel_avg', (255*kernel_avg/kernel_avg.max()).astype(np.uint8))
 
average = cv2.filter2D(src=image, ddepth=-1, kernel=kernel_avg)

cv2.imshow('Average', average)
cv2.waitKey(0)