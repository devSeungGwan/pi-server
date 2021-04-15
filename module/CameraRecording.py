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

    camera.start_preview()
    camera.start_recording("./{}/{}.h264".format(save_folder, capture_time))
    sleep(record_time)
    camera.stop_recording()
    camera.stop_preview()
    

if __name__ == "__main__":
    save_folder = sys.argv[1]
    record_time = int(sys.argv[2])
    width = int(sys.argv[3])
    height = int(sys.argv[4])
    frame_rate = int(sys.argv[5])

    camera_recording(save_folder, record_time, width, height, frame_rate)