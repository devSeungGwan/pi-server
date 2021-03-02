import picamera
import time
import datetime
import os


camera = picamera.PiCamera()
camera.resolution = (2592, 1944) # (64, 64) ~ (2592, 1944) px

for i in range(10):
    time.sleep(3)
    now = datetime.datetime.now()

    capture_folder = "/capture"
    capture_time = now.strftime("%Y-%m-%d_%H_%M_%S")
    capture_format = ".jpg"

    camera.capture('{}/{}{}'.format(capture_folder, capture_time, capture_format))
    print("Capture! : {}/{}{}".format(capture_folder, capture_time, capture_format))