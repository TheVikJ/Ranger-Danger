import cv2
import numpy as np
from datetime import datetime, timedelta
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
delay = datetime.now()

def jump():
    global delay
    if datetime.now() > delay:
        # Add code for the jump function here
        print("jump")
        keyboard.press(Key.up)
        time.sleep(0.1)
        keyboard.release(Key.up)
        delay = datetime.now() + timedelta(seconds=0.5)
        # A delay of 0.5 seconds is added between jumps
    
cap = cv2.VideoCapture(0)
_, frame = cap.read()
while True:
    _, frame = cap.read()
    if frame is not None:     
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Blue color
        low_blue = np.array([94, 80, 2])
        high_blue = np.array([126, 255, 255])
        blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
        # Masks out all colors except blue
        blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
        blue_perc = (blue_mask>0).mean()
        cv2.imshow("Blue", blue)
        # cv2.imshow("Frame", frame)
        if blue_perc<0.01:
            # If the percentage of blue in frame is less than 1%,
            # the jump funtion is called
            jump()
    key = cv2.waitKey(1)
    if key == 27:
        #If esc is clicked, the program is terminated
        break