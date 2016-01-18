import numpy as np
import cv2
import time
import serial


#ser = serial.Serial('/dev/ttyACM0', 9600)
#ser = serial.Serial('/dev/tty1' ,9600)
cap = cv2.VideoCapture(1)

bottompipe = cv2.CascadeClassifier("bottompipe_cascade.csv")
bird = cv2.CascadeClassifier("bird_cascade.csv")

x = 1  #frame counter

while(True):
    x = x+1
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if (x > 5):
	x = 0 
    	#rects = bottompipe.detectMultiScale(gray, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
    	rects = bottompipe.detectMultiScale(gray, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
	for (x,y,w,h) in rects:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    	rects = bird.detectMultiScale(gray, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
	for (x,y,w,h) in rects:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)

    	#if len(rects) > 0:
		##cv2.rectangle(frame,rects);
		#print "booom!!!!";
    		#curpos = rects[0,0]
		#if (curpos < 220):
			##ser.write('m')
			#print "m"
		#if (curpos > 280):
			#ser.write('p')
			#print "p"
		
    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
