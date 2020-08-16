from serial import Serial
from pynput.keyboard import Key, Controller
from time import sleep, time

jumpThreshold = 50
jumpDetectMin = 2

jumpDetects = 0
jumpNotDetects = 0

jump = False

jumpTime = 0

keyboard = Controller()

input("Start?")

with Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
    while True:
        distance = int(ser.readline())
        if distance > jumpThreshold:
            jumpDetects += 1
            jumpNotDetects = 0
        else:
            jumpDetects = 0
            jumpNotDetects += 1
            if jumpNotDetects > jumpDetectMin:
                jump = False

        if jumpDetects > 4 and not jump and jumpTime + 1 < time():
            print(f"{time()} jump")
            keyboard.press(Key.space)
            jumpTime = time()
            keyboard.release(Key.space)
            jump = True

