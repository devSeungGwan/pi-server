import cv2
import time
cap = cv2.VideoCapture(0)

while cap.isOpened():
  ret, img = cap.read()
  if ret:
    cv2.imshow('test', img)
    time.sleep(100)
    break