from django.db import models

class rpi_parameter(models.Model):
    idx = models.AutoField(primary_key=True)# 고유키
    save_folder = models.TextField()        # 저장 폴더 이름
    num_of_capture = models.IntegerField()  # 카메라 캡쳐 개수
    width = models.IntegerField()           # 이미지 가로 넓이
    height = models.IntegerField()          # 이미지 세로 넓이
    start_time = models.DateTimeField()     # 생성 시작 시간
    end_time = models.DateTimeField()       # 생성 종료 시간