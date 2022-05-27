import cv2
import mediapipe as mp
import keyboard


cap = cv2.VideoCapture(0)
MpHand = mp.solutions.hands
Hand = MpHand.Hands()
x = 0
y = 0
lm10 = 0.5

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    if results.multi_hand_landmarks:
        for Handlms in results.multi_hand_landmarks:
            for id, lm in enumerate(Handlms.landmark):
                if id == 0:
                    if 0.6 > lm.x > 0.4:
                        if x == 2:
                            keyboard.release("right")
                        if x == 1:
                            keyboard.release("left")
                    if lm.x > 0.6:
                        if x == 2:
                            keyboard.release("right")
                        keyboard.press("left")
                        x = 1
                    if lm.x < 0.4:
                        if x == 1:
                            keyboard.release("left")
                        keyboard.press("right")
                        x = 2
                    if lm.y > 0.7:
                        if y == 1:
                            keyboard.release("up")
                        keyboard.press("down")
                        y = 2
                    if lm.y < 0.7 and lm10 > 0.3:
                        if y == 1:
                            keyboard.release("up")
                        if y == 1:
                            keyboard.release("down")
                if id == 10:
                    lm10 = lm.y
                    if lm.y < 0.3:
                        if y == 1:
                            keyboard.release("down")
                        keyboard.press("up")
                        y = 1
                if id == 12:
                    if lm.y > lm10:
                        keyboard.send("space")