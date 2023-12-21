import cv2
import numpy as np
 
image = cv2.imread('angio.tif',0)

cv2.imshow('Original', image)
 
# Apply identity kernel
kernel = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])
 
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

cv2.imshow('Identity', identity)
cv2.waitKey(0)