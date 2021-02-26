import cv2
import numpy as np
 
img = cv2.imread("ngoc.jpg")
print(img.shape)
 
imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)

x = int(input())


imgCropped = img[0:x,200:500]
 
cv2.imshow("Image",img)
#cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
 
cv2.waitKey(0)