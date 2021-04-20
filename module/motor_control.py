import serial

def MotorContorl():
    ser = serial.Serial("/dev/ttyUSB0",9600)
    ser.write("2".encode('utf-8'))

if __name__ == "__main__":
    MotorContorl()