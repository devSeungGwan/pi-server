import picamera
import serial
import datetime
import os
from pprint import pprint


def camera_capture(config: dict, ser) -> str:
    camera = picamera.PiCamera()
    camera.resolution = (
        config["width"],
        config["height"],
    )  # (64, 64) ~ (2592, 1944) px

    capture_log = dict()
    capture_log["capture_config"] = config
    save_folder = config["capture_folder"]

    ser_capture = 1

    while True:
        if ser.readable():
            res = ser.readline()
            res = res.decode().strip()

            if res == "CAPTURE":
                now = datetime.datetime.now()
                capture_time = now.strftime("%Y-%m-%d_%H_%M_%S")
                capture_format = "jpg"
                file_name = os.path.join(save_folder, "{}.{}".format(capture_time, capture_format))
                camera.capture(file_name)

                capture_log[ser_capture] = {
                    "file name": file_name,
                    "capture time": capture_time,
                }

                ser_capture += 1

                pprint(
                    "📸 Capture! : ./{}/_{}{}".format(
                        save_folder, capture_time, capture_format
                    )
                )

            elif res == "END":
                now = datetime.datetime.now()
                capture_time = now.strftime("%Y-%m-%d_%H_%M_%S")
                break

    camera.close()

    return capture_log
