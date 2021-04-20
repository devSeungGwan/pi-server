# import picamera
import time
import datetime
import os
import sys
import serial
from pprint import pprint


def camera_caputure(save_folder: str, num_of_capture: int, width: int, height: int) -> str:
    camera = picamera.PiCamera()
    camera.resolution = (width, height)  # (64, 64) ~ (2592, 1944) px
    camera.start_preview()

    now = datetime.datetime.now()
    start_time = now.strftime("%Y-%m-%d_%H_%M_%S")

    try:
        os.makedirs("./{}".format(save_folder))
    except:
        pass
    
    log = { 
        "save_folder": save_folder,
        "start_time": start_time,
        "num_of_capture": num_of_capture,
        "px": camera.resolution,
    }

    for i in range(num_of_capture):
        now = datetime.datetime.now()
        capture_time = now.strftime("%Y-%m-%d_%H_%M_%S")
        capture_format = ".jpg"
        file_name = "./{}/_{}{}".format(save_folder, capture_time, capture_format)
        camera.capture(file_name)

        log[i + 1] = {
            "file name": file_name,
            "capture time": capture_time,
        }

        pprint(
            "Capture! : ./{}/_{}{}".format(save_folder, capture_time, capture_format)
        )

    camera.close()

    return log

def openSerial(port, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False):
    ser = serial.Serial()

    ser.port = port
    ser.baudrate = baudrate
    ser.bytesize = bytesize
    ser.parity = parity
    ser.stopbits = stopbits
    ser.timeout = timeout
    ser.xonxoff = xonxoff
    ser.rtscts = rtscts
    ser.dsrdtr = dsrdtr

    ser.open()
    return ser


def MotorContorl():
    ser = openSerial("com9")
    ser.write(b"a")


if __name__ == "__main__":
    # save_folder = str(sys.argv[1])
    # num_of_folder = int(sys.argv[2])
    # width = int(sys.argv[3])
    # height = int(sys.argv[4])

    # pprint(camera_caputure(save_folder, num_of_folder, width, height))

    MotorContorl()
