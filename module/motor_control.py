import serial

# def MotorContorl():
#     ser = serial.Serial("/dev/ttyUSB0",115200)
#     ser.write("2".encode('utf-8'))

if __name__ == "__main__":
    ser = serial.Serial("/dev/ttyUSB0",9600)
    while True:
        if ser.readable():
            res = ser.readline()
            print(res.decode())