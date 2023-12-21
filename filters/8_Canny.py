import numpy as np
import cv2


image = cv2.imread('angio.tif',0)
cv2.imshow('Original image', image)
cv2.waitKey(0)

edges = cv2.Canny(image,100,150)

cv2.imshow('Canny', edges)
cv2.waitKey(0)