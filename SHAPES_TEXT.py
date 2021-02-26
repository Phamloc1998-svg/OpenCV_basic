import cv2
import numpy as np

# img = cv2.imread('ngoc.jpg')
img = np.zeros((480, 480, 3),np.uint8)
#print(img)
#img[:]= 255,0,0
 
cv2.line(img,(0,0),(img.
shape[1], img.shape[0]),(255,255,0),3)
cv2.rectangle(img,(100,100),(250,250),(0,0,255),2)
cv2.circle(img,(100,100),10,(255,255,0),3)
cv2.putText(img,"LoveNgoc",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)

cv2.imshow("Image",img)
cv2.waitKey(0)