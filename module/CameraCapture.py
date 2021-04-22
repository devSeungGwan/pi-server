import picamera
import serial

import time
import datetime
import os
import sys
from pprint import pprint


def camera_capture(width: int, height: int, ser) -> str:
    camera = picamera.PiCamera()
    camera.resolution = (width, height)  # (64, 64) ~ (2592, 1944) px

    now = datetime.datetime.now()
    start_time = now.strftime("%Y-%m-%d_%H_%M_%S")

    try:
        os.makedirs("./{}".format(start_time))
    except:
        pass
    
    log = { 
        "save_folder": start_time,
        "num_of_capture": 24,
        "px": camera.resolution,
    }

    ser_capture = 0

    while True:
        if ser.readable() : 
            res = ser.readline()
            res = res.decode().strip()

            if(res == "CAPTURE"):
                now = datetime.datetime.now()
                capture_time = now.strftime("%Y-%m-%d_%H_%M_%S")
                capture_format = ".jpg"
                file_name = "./{}/_{}{}".format(start_time, capture_time, capture_format)
                camera.capture(file_name)

                log[ser_capture + 1] = {
                    "file name": file_name,
                    "capture time": capture_time,
                }

                ser_capture += 1
                
                pprint(
                    "Capture! : ./{}/_{}{}".format(start_time, capture_time, capture_format)
                )  
                
            elif(res == "END"):
                now = datetime.datetime.now()
                capture_time = now.strftime("%Y-%m-%d_%H_%M_%S")
                print("Capture End: {}".format(capture_time))
                break     

    camera.close()

    return log

if __name__ == "__main__":
    width = int(sys.argv[1])
    height = int(sys.argv[2])

    ser = serial.Serial("/dev/ttyUSB0",9600)
    while True:
        if ser.readable():
            res = ser.readline()
            res = res.decode().strip()

            now = datetime.datetime.now()
            start_time = now.strftime("%Y-%m-%d_%H_%M_%S")

            if(res == "START"):
                print("Capture Start: {}".format(start_time))
                camera_capture(width, height, ser)
