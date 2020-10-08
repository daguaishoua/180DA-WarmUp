import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap.open()

while(True):
    _, frame = cap.read()

    lower_red = np.array([163, 40, 40])
    upper_red = np.array([224, 92, 92])

    mask = cv2.inRange(frame, lower_pink, upper_pink)

    res = cv2.bitwise_and(frame, frame, mask= mask)
    # Adaptive thresholding on mask to convert to a binary image to make finding contours easier
    thresh = cv2.adaptiveThreshold(mask, 125, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)

    # Try to eliminate background detection by looking for significant patches of color
    for i in contours:
        if cv2.contourArea(i) > 200:
            x, y, w, h = cv2.boundingRect(i)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display video streams
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
