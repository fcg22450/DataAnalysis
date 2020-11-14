import os,time,json, redis
from .models import FileData_000000,FileDataDriving,FileDataParking,FileDataRadar,FileDataVideo,FileType,BaseFilePath,Labels
# 定时任务创建
# 定时获取json文件情况来进行数据更新

def create_db_data():
    db_table_list = [
        FileData_000000(),
        FileDataDriving(),
        FileDataParking(),
        FileDataRadar(),
        FileDataVideo()
    ]
    db_create = Data_create_db()
    for index,db in enumerate(db_table_list):
        db_create.data_save(db,index)

class Data_create_db:
    def __init__(self):
        self.data_000000_file = open('./data_000000_file.json', 'r')
        self.data_driving_file = open('./data_driving_file.json', 'r')
        self.data_parking_file = open('./data_parking_file.json', 'r')
        self.data_radar_file = open('./data_radar_file.json', 'r')
        self.data_video_file = open('./data_video_file.json', 'r')

    # 对数据进行处理
    def data_save(self, db, db_number):
        # 传入的参数为调用的数据库的名字和编号
        if db_number == 0:
            file_data = json.load(self.data_000000_file)
        elif db_number ==1:
            file_data = json.load(self.data_driving_file)
        elif db_number ==2:
            file_data = json.load(self.data_parking_file)
        elif db_number ==3:
            file_data = json.load(self.data_radar_file)
        elif db_number ==4:
            file_data = json.load(self.data_video_file)
        for data in file_data:
            db.file_name = data['file_name']
            db.file_type = data['file_type']
            db.file_size = data['file_size']
            db.file_time = data['file_time']
            db.file_path = data['file_path']
            db.file_create_time = data['file_create_time']
            db.file_update_time = data['file_update_time']
            db.is_delete = data['is_delete']
            db.is_delete = data['is_delete']
            db.save()

    def __del__(self):
        self.data_000000_file.close()
        self.data_driving_file.close()
        self.data_parking_file.close()
        self.data_radar_file.close()
        self.data_video_file.close()