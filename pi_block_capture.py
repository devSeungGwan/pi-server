import picamera
import time
import datetime
import os
import sys

def pi_picture(capture_folder):
    camera = picamera.PiCamera()
    camera.resolution = (800, 800) # (64, 64) ~ (2592, 1944) px
    camera.start_preview()
    
    try:
        os.makedirs("./{}".format(capture_folder))
    except:
        pass
    

    for i in range(10):
        time.sleep(1)
        now = datetime.datetime.now()

        capture_time = now.strftime("%Y-%m-%d_%H_%M_%S")
        capture_format = ".jpg"

        camera.capture('{}/_{}{}'.format(capture_folder, i, capture_format))
        print("Capture! : {}/_{}{}".format(capture_folder, i, capture_format))
    
    camera.close()

    return {
        "capture folder": capture_folder,
        "image cnt": 10
    }