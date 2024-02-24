import cv2
import numpy as np

video = "source-video-2.mp4"
cap = cv2.VideoCapture(video)
while(1):
    _, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 110, 150])
    upper_red = np.array([9, 255, 255])

    lower_green = np.array([45, 60, 100])
    upper_green = np.array([75, 255, 255])

    mask_red = cv2.inRange(hsv_frame, lower_red, upper_red)
    mask_green = cv2.inRange(hsv_frame, lower_green, upper_green)

    res_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    res_green = cv2.bitwise_and(frame, frame, mask=mask_green)

    combined_res = cv2.add(res_red, res_green)

    cv2.imshow('result', combined_res)

    if cv2.waitKey(25) & 0xFF == ord('q'):  
        break

cv2.destroyAllWindows()
