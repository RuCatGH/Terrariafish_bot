from ctypes import windll, Structure, c_long, byref

import time
import cv2
import mss
import numpy as np

import pyautogui


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {"x": pt.x, "y": pt.y}


def click():
    pyautogui.mouseDown()
    time.sleep(0.01)
    pyautogui.mouseUp()


# 800x600 game window (based on 3440x1440 screen resolution)
# mon = {"top": 420, "left": 1320, "width": 800, "height": 600}

title = "Terraria Auto-Fishing"
sct = mss.mss()

print("STARTING after 15 seconds, please adjust your rod!")
time.sleep(10)
print("Started ...")

click()
print("Rod dropped ...")
last_time = time.time()  # time last fish was catched


while True:
    # must be at least 2 seconds before last catch
    if time.time() - last_time < 2:
        continue

    cur = queryMousePosition()
    mon = {"top": cur['y'] - 5, "left": cur['x'] -
           5, "width": 10, "height": 10}
    img = np.asarray(sct.grab(mon))

    #cv2.imshow(title, img)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        quit()

    # create hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # lower mask (0-10)
    lower_red = np.array([9, 72, 112])
    upper_red = np.array([133, 209, 234])
    mask0 = cv2.inRange(hsv, lower_red, upper_red)

    # join masks
    mask = mask0

    # check
    hasRed = np.sum(mask)
    if hasRed > 0:
        # print("RED detected!") # do nothing
        pass
    else:
        # print("RED NOT detected!") # catch!

        # get the stuff
        print("Catch! ...")
        time.sleep(0.8)
        click()

        time.sleep(0.5)  # wait some
        print("New rod dropped ...")
        click()

        last_time = time.time()  # time last fish was catched
