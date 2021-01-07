import numpy as np # pip install numpy
import pyautogui as pg # pip install pyutogui
import cv2 # pip install opencv-python

cc = cv2.VideoWriter_fourcc(*"XVID")
size = pg.size()
output = cv2.VideoWriter("Recorded.avi", cc, 20.0, size)

while True:
    image = pg.screenshot()
    frames = np.array(image)
    frames = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
    output.write(frames)
    cv2.imshow("Recorder_with_python", frames)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
output.release()
