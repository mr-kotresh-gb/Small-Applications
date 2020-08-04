import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)  # 0 is for webcam. If we using multiple cameras then we can choose them also
# Here we can give recorded video also
time.sleep(3)
background = 0

for i in range(30):  # Im giving 30 iterations to capture background correctly and get perfect image of bg
    ret, background = cap.read()


while cap.isOpened():
    ret, img = cap.read()  # Here Im capturing to perform operations
    if not ret:
        break
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)  # Separating clock part

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2  # bitwise OR

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)  #Noise removel
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=2)
    mask2 = cv2.bitwise_not(mask1)  # Except the clock

    res1 = cv2.bitwise_and(background, background, mask=mask1)  # Used for the segmentation of the color
    res2 = cv2.bitwise_and(img, img, mask=mask2)  # Used to substitute the clock part
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)  # alpha(1st source) beta(2nd source) gama

    cv2.imshow('Kotresh !', final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()