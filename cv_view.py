import cv2
cap = cv2.VideoCapture(0)

while cap.isOpened():
  ret, img = cap.read()
  if ret:
    cv2.imshow('test', img)
    if cv2.waitkey(1) & 0xFF == 27: # esc
      break