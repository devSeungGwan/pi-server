import os
import datetime
import json


def make_folder(root_folder: str, block_name: str):
    res_code = 0
    folder = os.path.join(root_folder, block_name)

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
    now = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    sep = {0: "start", 1: "end"}
    return "👌 Capture {}: {}".format(sep[code], now)


def save_log(log: dict):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    with open("{}.json".format(now), "w", encoding="utf-8") as json_file:
        json.dump(log, json_file)
