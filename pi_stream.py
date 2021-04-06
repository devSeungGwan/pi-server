import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (2592, 1944)

camera.start_preview()
time.sleep(100)
camera.close()
