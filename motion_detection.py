import imutils
import numpy as np
import cv2
import time
from time import sleep


cap = cv2.VideoCapture('C:/Users/rgukt/Desktop/vid.mp4')       # Reading the video file

previous_image = None
print('haii')
while cap.isOpened():
    start = time.time()
    for i in range(0,10):
        ret, frame = cap.read()
    
        if ret:
            
                gray = cv2.cvtColor(frame, 0)
            
             
                resized_image1 = cv2.resize(gray, (300, 300)) 
            

                if previous_image is not None:
               
                    pass
                previous_image = resized_image1
                ret, frame = cap.read()
                sleep(0.1)
                gray1 = cv2.cvtColor(frame, 0)
                resized_image = cv2.resize(gray1, (300, 300))

                difference = cv2.absdiff(resized_image, previous_image)      # difference between current and previous frame
                #print(difference.shape)

                gray_image = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
                (thresh, im_bw) = cv2.threshold(gray_image ,50,250, cv2.THRESH_BINARY)[:] #setting the threshold
                
                
                _ ,contours, _ = cv2.findContours(im_bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   ##finding the contours
                final_image = cv2.resize(frame,(300,300))
                cv2.drawContours(final_image, contours, -1, (0,255,0), 1)
                
                for c in contours:
                  if count==100:
                    pass
                  (x, y, w, h) = cv2.boundingRect(c)
                  cv2.rectangle(final_image, (x, y), (x + w, y + h), (0, 255, 0), 1)       ##Drawing the rectangulr boxes
		  
                  
                cv2.imshow('frame1',final_image)
                
        
        #if cv2.waitKey(1) & 0xFF == ord('q'):
         #  break


cap.release()
cv2.destroyAllWindows()
