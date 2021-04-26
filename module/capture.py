import picamera
import serial
import datetime
import os
from pprint import pprint


def camera_capture(save_folder: str, width: int, height: int, ser) -> str:
    camera = picamera.PiCamera()
    camera.resolution = (width, height)  # (64, 64) ~ (2592, 1944) px

    log = {
        "save_folder": save_folder,
        "px": camera.resolution,
    }

    ser_capture = 1

    while True:
        if ser.readable():
            res = ser.readline()
            res = res.decode().strip()

            if res == "CAPTURE":
                now = datetime.datetime.now()
                capture_time = now.strftime("%Y-%m-%d_%H_%M_%S")
                capture_format = ".jpg"
                file_name = "./{}/_{}{}".format(
                    save_folder, capture_time, capture_format
                )
                camera.capture(file_name)

                log[ser_capture] = {
                    "file name": file_name,
                    "capture time": capture_time,
                }

                ser_capture += 1

                pprint(
                    "Capture! : ./{}/_{}{}".format(
                        save_folder, capture_time, capture_format
                    )
                )

            elif res == "END":
                now = datetime.datetime.now()
                capture_time = now.strftime("%Y-%m-%d_%H_%M_%S")
                break

    camera.close()

    return log
