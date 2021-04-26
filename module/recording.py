from picamera import PiCamera
from time import sleep
import datetime
import sys
import os

def camera_recording(save_folder: str, record_time: int, width: int, height: int, frame_rate: int):
    camera = PiCamera()

    # camera parameter setting
    camera.resolution = (width, height)
    camera.framerate = frame_rate

    # make folder
    try:
        os.makedirs("./{}".format(save_folder))
    except:
        pass
    
    now = datetime.datetime.now()
    capture_time = now.strftime("%Y-%m-%d_%H_%M_%S")

    camera.start_recording("./{}/{}.h264".format(save_folder, capture_time))
    sleep(record_time)
    camera.stop_recording()