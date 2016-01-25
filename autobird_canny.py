import numpy as np
import cv2
import time
import serial


ser = serial.Serial('/dev/ttyACM0', 9600)
#ser = serial.Serial('/dev/tty1' ,9600)
cap = cv2.VideoCapture(1)

bottompipe = cv2.CascadeClassifier("screenpipe.csv")
bird = cv2.CascadeClassifier("birdeye_cascade.csv")
framenum=1
x = 1  #frame counter

birddetect = 0

while(True):
    x = x+1
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray,(5,5),0)	
    bw = cv2.Canny(blur, 0, 100, 5)


    cv2.imwrite("./pics/cannysnap" + str(framenum) + ".jpg", bw)
    framenum += 1
    tempx = 0

   #rects = bottompipe.detectMultiScale(gray, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
    rects = bottompipe.detectMultiScale(gray, 10, 5)

    rects = bird.detectMultiScale(gray, 2.5, 5, cv2.cv.CV_HAAR_SCALE_IMAGE, (17,18))
    for (x,y,w,h) in rects:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)

    
    # Display the resulting frame
    cv2.imshow('frame',frame)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
    if cv2.waitKey(1) & 0xFF == ord('t'):
	ser.write('t')
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
