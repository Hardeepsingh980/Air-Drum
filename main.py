import cv2
import numpy as np
from pygame import mixer
import _thread

mixer.init()


def play_cords(file):
    mixer.music.load(file)
    mixer.music.play()



cap = cv2.VideoCapture(1)

while cap.isOpened():
    _, img = cap.read()
    img = cv2.resize(img,(300,300))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



    l_b = np.array([30,151,32])
    u_b = np.array([83,255,255])

    mask = cv2.inRange(hsv,l_b, u_b)

    res = cv2.bitwise_and(img,img,mask=mask)


    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        (x,y,w,h) = cv2.boundingRect(c)
        if cv2.contourArea(c) < 100:
            continue
        else:
            cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),2)
            
            if x > 0 and y > 230  and x < 90 and y < 250  :                
                cv2.putText(img, 'A',(10,20),cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),3)
                _thread.start_new_thread(play_cords,('Cords/A.mp3',))

            elif x > 91 and y > 230  and x < 180 and y < 250  :                
                cv2.putText(img, 'B',(10,20),cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),3)
                _thread.start_new_thread(play_cords,('Cords/B.mp3',))

            elif x > 181 and y > 230  and x < 300 and y < 250  :                
                cv2.putText(img, 'C',(10,20),cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),3)
                _thread.start_new_thread(play_cords,('Cords/C.mp3',))

            

    cv2.drawContours(img, contours, -1, (0,0,255),2)

    img = cv2.line(img, (90,250),(90,400),(255,0,0),3)

    img = cv2.line(img, (180,250),(180,400),(255,0,0),3)
    
    
    
    cv2.imshow('image',img)
##    cv2.imshow('mask',mask)
##    cv2.imshow('res',res)
    
    k = cv2.waitKey(1)
    if k ==ord('q'):
        break
    if k ==27:
        break

    
cv2.destroyAllWindows()
