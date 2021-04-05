import picamera
import time
import datetime
import os
import sys
from pprint import pprint

def pi_picture(save_folder):
    camera = picamera.PiCamera()
    camera.resolution = (800, 800) # (64, 64) ~ (2592, 1944) px
    camera.start_preview()
    
    now = datetime.datetime.now()
    start_time = now.strftime("%Y-%m-%d_%H_%M_%S")

    try:
        os.makedirs("./{}".format(save_folder))
    except:
        pass
    
    log = {
        "save_folder": save_folder,
        "start_time": start_time
    }

    for i in range(10):
        time.sleep(4)
        now = datetime.datetime.now()

        capture_time = now.strftime("%Y-%m-%d_%H_%M_%S")
        capture_format = ".jpg"
        file_name = './{}/_{}{}'.format(save_folder, capture_time, capture_format)
        camera.capture(file_name)
        log[i+1] = {
            "file name": file_name,
            "capture time": capture_time,
        }
        pprint("Capture! : ./{}/_{}{}".format(save_folder, capture_time, capture_format))
    
    camera.close()

    return log

if __name__ == "__main__":
    pprint(pi_picture(sys.argv[1])) 