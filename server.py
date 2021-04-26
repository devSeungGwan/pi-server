from module.capture import camera_capture
from module.util import make_folder, capture_time, save_log
from module.config import block_config
import serial

if __name__ == "__main__":
    config = block_config()
    config_data = config.get_data()

    ser = serial.Serial(
        config_data["serial_config"]["serial_name"],
        config_data["serial_config"]["serial_port"],
    )

    while True:
        # 아두이노에서 촬영 신호가 왔을 경우,
        if ser.readable():
            res = ser.readline()
            res = res.decode().strip()

            if res == "START":
                # 촬영 시작 시간 체크
                print(capture_time(0))

                # 폴더 생성
                folder = make_folder(
                    config_data["capture_config"]["root_folder"],
                    config_data["capture_config"]["block_name"],
                )

                # 카메라 캡쳐
                log = camera_capture(config_data["capture_config"], ser)

                # 로그 저장
                save_log(log)

                # 촬영 종료 시간 체크
                print(capture_time(1))
