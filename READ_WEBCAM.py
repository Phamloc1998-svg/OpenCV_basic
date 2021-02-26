import cv2
Width = 640 
Height = 480
cap = cv2.VideoCapture(0)
cap.set(3, Width)
cap.set(4, Height)
cap.set(10, 150)
while True:
    success, img = cap.read()
    cv2.imshow("loc",img)
    if cv2.waitKey(1) and 0xff == ord('q'):
        break