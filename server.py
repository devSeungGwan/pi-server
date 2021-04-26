import sys
from module.capture import camera_capture
from module.util import make_folder, capture_time
import serial


if __name__ == "__main__":
    width = int(sys.argv[1])
    height = int(sys.argv[2])

    ser = serial.Serial("/dev/ttyUSB0", 9600)

    while True:
        if ser.readable():
            res = ser.readline()
            res = res.decode().strip()

            if res == "START":
                print(capture_time(0))
                folder = make_folder()
                camera_capture(folder["folder_src"], width, height, ser)
                print(capture_time(1))
