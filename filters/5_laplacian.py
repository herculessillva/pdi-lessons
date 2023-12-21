#import matplotlib.pyplot as plt
import numpy as np
import cv2


image = cv2.imread('angio.tif',0)
cv2.imshow('Original image', image)
cv2.waitKey(0)

#Laplacian masks
lpc_1 = np.array([[0,1,0],[1,-4,1],[0,1,0]])
lpc_2 = np.array([[0.25,0.5,0.25],[0.5,-3,0.5],[0.25,0.5,0.25]])
lpc_3 = np.array([[1,1,1],[1,-8,1],[1,1,1]])

lpc = [lpc_1, lpc_2, lpc_3]

for i in range(len(lpc)):
    lpc_im = cv2.filter2D(src=image, ddepth=-1, kernel=lpc[i])
    cv2.imshow('Laplacian_image_filter_mask_'+str(i+1), lpc_im)
    cv2.waitKey(0)