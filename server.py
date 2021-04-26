from module.capture import camera_capture
from module.util import make_folder, capture_time, save_log
from module.config import block_config
import serial

if __name__ == "__main__":
    print("🚗 Running RPi Camera Capture Server...")

    config = block_config()
    config_data = config.get_data()

    ser = serial.Serial(
        config_data["serial_config"]["serial_name"],
        config_data["serial_config"]["serial_port"],
    )

    while True:
        print("1. 👆 Click Start Button")
        print("2. 🔄 Change Block Name")
        print("3. 🖐 Exit")
        select = input("Select: ")

        # 블록 촬영
        if select == "1":
            print("👆 Please Click Start Button...")
            while True:
                # 아두이노에서 촬영 신호가 왔을 경우,
                if ser.readable():
                    res = ser.readline()
                    res = res.decode().strip()

                    if res == "START":
                        # 촬영 시작 시간 체크
                        print(capture_time(0))

                        # 폴더 생성
                        config_data["capture_config"]["capture_folder"] = make_folder(
                            config_data["capture_config"]["root_folder"],
                            config_data["capture_config"]["block_name"],
                        )

                        # 카메라 캡쳐
                        log = camera_capture(config_data["capture_config"], ser)

                        # 로그 저장
                        save_log(log)

                        # 촬영 종료 시간 체크
                        print(capture_time(1))
                        print("\n")
                    
                    break

        # 블록 이름 변경
        elif select == "2":
            block_name = input("Enter Block Name: ")
            config_data["capture_config"]["block_name"] = block_name
            print("🔄 Change Block: {}\n".format(block_name))

        # 종료
        elif select == "3":
            print("🖐 Good Bye")
            exit()