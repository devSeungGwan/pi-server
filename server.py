from module.capture import camera_capture
from module.util import make_folder, capture_time, save_log
from module.config import block_config
import serial

if __name__ == "__main__":
    print("🚗 Running RPi Camera Capture Server...\n")

    config = block_config()
    config_data = config.get_data()

    ser = serial.Serial(
        config_data["serial_config"]["serial_name"],
        config_data["serial_config"]["serial_port"],
    )

    while True:
        print("📖 Select Memu")
        print("1. 👆 Click Start Button")
        print("2. 🔄 Change Block Name")
        print("3. 🛠 config")
        print("4. 🖐 Exit")
        select = input("Select: ")
        print("\n")

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
        
        # 촬영 옵션 변경
        elif select == "3":
            print("1. 📂 capture folder")
            print("2. ↔ width")
            print("3. ↕ height")
            print("4. auto exposure")
            print("5. iso")
            print("6. shutter speed")
            print("7. back to menu")
            cfg_select = input("Select: ")

            if cfg_select == "1":
                folder_name = input("\nCapture folder name: ")
                config.set_data("capture_config", "root_folder", folder_name)
                print("Change folder name: {}\n".format(folder_name))

            elif cfg_select == "2":
                width = input("\nChange width: ")
                if(not width.isdigit()):
                    print("올바른 값을 입력하지 않았습니다. 처음으로 돌아갑니다.\n")
                else:
                    config.set_data("capture_config", "width", int(width))
                    print("Change width: {}\n".format(int(width)))

            elif cfg_select == "3":
                height = input("\nChange height: ")
                if(not height.isdigit()):
                    print("올바른 값을 입력하지 않았습니다. 처음으로 돌아갑니다.\n")
                else:
                    config.set_data("capture_config", "height", int(height))
                    print("Change height: {}\n".format(int(height)))
            elif cfg_select == "4":
                expo_mode = input("1. ON, 2. OFF")
                if expo_mode == "1":
                    config.set_data("capture_config", "auto_exposure", "on")
                    print("change auto exposure: ON\n")
                elif expo_mode == "2":
                    config.set_data("capture_config", "auto_exposure", "off")
                    print("change auto exposure: OFF\n")
                else:
                    print("올바른 값을 입력하지 않았습니다. 처음으로 돌아갑니다.\n")

            elif cfg_select == "5":
                iso = input("\nChange iso: ")
                if(not iso.isdigit()):
                    print("올바른 값을 입력하지 않았습니다. 처음으로 돌아갑니다.\n")
                else:
                    config.set_data("capture_config", "iso", int(iso))
                    print("Change iso: {}\n".format(int(iso)))

            elif cfg_select == "6":
                shutter_speed = input("\nChange shutter speed: ")
                if(not shutter_speed.isdigit()):
                    print("올바른 값을 입력하지 않았습니다. 처음으로 돌아갑니다.\n")
                else:
                    config.set_data("capture_config", "shutter_speed", int(shutter_speed))
                    print("Change shutter speed: {}\n".format(int(shutter_speed)))

            elif cfg_select == "7":
                print("\n")

        # 종료
        elif select == "4":
            print("🖐 Good Bye!!\n")
            exit()