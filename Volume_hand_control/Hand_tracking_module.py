import cv2
import mediapipe as mp
import time



cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils


#Variable for FPS
PTime = 0
CTime = 0


while True:


    #Reading the CV2 module
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


    #print(success)
    result = hands.process(imgRGB)
    #print(result.multi_hand_landmarks)


    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                print(id)
                print(lm)
            mpdraw.draw_landmarks(img,handLms,mphands.HAND_CONNECTIONS)

    CTime = time.time()
    fps = 1/(CTime-PTime)
    PTime = CTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (100, 100, 0), 3)

    cv2.imshow("Image",img)
    cv2.waitKey(1)
