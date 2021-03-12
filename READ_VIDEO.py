# import cv2
# frameWidth = 640
import cv2
#khai bao hight, width
frameWidth = 640
frameHight = 480
#Video capture source
cap = cv2.VideoCapture('contraiHDFA.mp4')
#Tao vong lap doc
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHight))
    cv2.imshow('HDPA', img)
    if cv2.waitKey(1) and 0xFF == ord ('q'):
        break