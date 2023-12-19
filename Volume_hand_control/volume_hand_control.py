import cv2
import numpy as np
import time
import Hand_tracking_module as htm

############### Declaring the width and height of the camera ;)
Wcam, Hcam = 1280,720
#################


########## variable for FPS
PTime = 0

#Capturing the Video(This is main command to assign 'cap' to the video capture) ;)
cap = cv2.VideoCapture(0)

########### Assigning the Width and Height of the Camera
cap.set(3,Wcam)
cap.set(4,Hcam)


while True:
    ### Using the Camera
    success ,img = cap.read()

    #### Showing the Number of Frames
    CTime = time.time()
    fps = 1/(CTime-PTime)
    PTime = CTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (100, 100, 0), 3)

    #### Showing the Camera on Window
    cv2.imshow("Image",img)
    cv2.waitKey(1)

