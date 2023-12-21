import numpy as np
import cv2


image = cv2.imread('angio.tif')
cv2.imshow('Original', image)
cv2.waitKey(0)

h_mask = np.array([[-1,0,1],[-1,0,1],[-1,0,1]]) #Filtro horizontal
v_mask = np.array([[-1,-1,-1],[0,0,0],[1,1,1]]) #Filtro vertical

img_h_filter = cv2.filter2D(src=image, ddepth=-1, kernel=h_mask)
cv2.imshow('Prewitt Horizontal', img_h_filter)
cv2.waitKey(0)

img_v_filter = cv2.filter2D(src=image, ddepth=-1, kernel=v_mask)
cv2.imshow('Prewitt Vertical', img_v_filter)
cv2.waitKey(0)

img_filter = np.sqrt(img_h_filter**2 + img_v_filter**2).astype(np.uint8)
cv2.imshow('Prewitt Global', img_filter)
cv2.waitKey(0)