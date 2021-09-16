from imutils.video import FPS
import cv2
import numpy as np 
import pyautogui
import imutils

SCREEN_SIZE = (2560,1440)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("gravação.avi", fourcc, 20.0, (SCREEN_SIZE))

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.waitKey(100)
cv2.destroyAllWindows
out.release()
