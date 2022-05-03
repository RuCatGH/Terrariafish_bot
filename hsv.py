import cv2
import numpy as np
cat_image = cv2.imread('photo.jpg')
cat_hsv = cv2.cvtColor(cat_image, cv2.COLOR_BGR2HSV)  # Преобразуем в HSV
low_red = (9, 72, 112)

high_red = (133, 209, 234)
only_cat = cv2.inRange(cat_hsv, low_red, high_red)
cv2.imshow('only cat', only_cat)
cv2.waitKey(0)
cv2.imwrite('photo1.jpg', only_cat)
