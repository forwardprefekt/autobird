import numpy as np
import cv2
import time
import serial


#ser = serial.Serial('/dev/ttyACM0', 9600)
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
    if (x > 2):
	x = 0 
	#cv2.imwrite("snap" + str(framenum) + ".jpg", frame)
    	framenum += 1
	tempx = 0

    	#rects = bottompipe.detectMultiScale(gray, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
    	rects = bottompipe.detectMultiScale(gray, 10, 5)
	firstcol = np.array(rects)
	firstcol = np.sort(firstcol,0)
	print firstcol

	for (x,y,w,h) in rects:

		if tempx > 0:
			if tempx + tempw > x + 50: #newcol
				break;

			if tempy + temph > y + 100:
				curcolheight = tempy + temph
				cv2.rectangle(frame,(tempx,tempy),(temph,tempw),(255,255,255),2)

		tempx = x
		tempy = y		
		temph = h
		tempw = w



	
	for (x,y,w,h) in rects:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
		
		

    	rects = bird.detectMultiScale(gray, 2.5, 5, cv2.cv.CV_HAAR_SCALE_IMAGE, (17,18))
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
