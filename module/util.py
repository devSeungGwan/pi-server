import os
import datetime


def make_folder():
    now = datetime.datetime.now()
    start_time = now.strftime("%Y-%m-%d_%H_%M_%S")
    folder = "./{}".format(start_time)
    res_code = 0

    # 폴더 생성
    try:
        os.makedirs(folder)
        print("Create folder: {}".format(folder))
        res_code = 1

    # 폴더가 이미 존재하는 경우
    except:
        print("Folder is already created: {}".format(folder))
        res_code = 2

    return {"folder_src": folder, "res_code": res_code}


def capture_time(code: int):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    sep = {0: "start", 1: "end"}
    return "Capture {}: {}".format(sep[code], now)