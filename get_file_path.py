import os
# # 获取文件时长的模块
from moviepy.editor import VideoFileClip
# '''

# \\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Driving
# \\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Parking
# \\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Radar
# \\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Video
# '''
import time
import json

'''
class RefreshData:
    def __init__(self):
        if os.path.exists('./data_fingerprint_file.json'):
            self.f = open('./data_fingerprint_file.json', 'r')
            self.f_data = json.load(self.f)
            # if self.f:
            #     print(self.f)
            #     # self.f_data = json.load(self.f)
            # else:
            #     self.f_data = {}
        else:
            self.f = open('./data_fingerprint_file.json', 'w')
            self.f_data = {}
        self.path = r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA'
        self.movie_types = (
            '.mp4', 
            '.mkv', 
            '.avi', 
            # '.wmv', 
            '.iso')
        self.file_data_list = [
            r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\000000', 
            r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Driving', 
            r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Parking', 
            r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Radar', 
            r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Video']
        self.get_dirs_data()
        self.write_data()
    def write_data(self):
        with open('./data_fingerprint_file.json', 'w') as f:
            json.dump(self.f_data, f)
    def get_dirs_data(self):
        def print_dir_constents(dir_path):
            try:
                for schild in os.listdir(dir_path if os.path.exists(dir_path) else False):
                    
                    #拼接地址
                    data_dict = {}
                    sChildPath = os.path.normpath("{}\{}".format(dir_path, schild))
                    # print(sChildPath)
                    # print(sChildPath)
                    # 文件创建时间
                    file_create_time = time.localtime(os.path.getctime(sChildPath)) if os.path.exists(sChildPath) else '0-0-0-0-0-0'
                    if type(file_create_time) == str:
                        # print('未获取到文件创建时间')
                    else:
                        # print(file_create_time)
                        file_create_time = str(file_create_time.tm_year) + '-' + str(file_create_time.tm_mon) + '-' + str(file_create_time.tm_mday) + '-' + str(file_create_time.tm_hour) + '-' + str(file_create_time.tm_min) + '-' + str(file_create_time.tm_sec)
                    # 文件修改时间
                    # print(file_create_time)
                    file_update_time = time.localtime(os.path.getmtime(sChildPath)) if os.path.exists(sChildPath) else '0-0-0-0-0-0'
                    if type(file_update_time) == str:
                        # print('未获取到文件修改时间')
                    else:
                        # print(file_update_time)
                        file_update_time = str(file_update_time.tm_year) + '-' + str(file_update_time.tm_mon) + '-' + str(file_update_time.tm_mday) + '-' + str(file_update_time.tm_hour) + '-' + str(file_update_time.tm_min) + '-' + str(file_update_time.tm_sec)
                    # 文件类型和文件名
                    files=os.path.splitext(sChildPath)
                    file_name,file_type=files
                    # 文件名
                    file_name = file_name.split('\\')[-1]
                    # 文件类型
                    file_type = file_type if file_type else 'File folder'
                    # 文件大小
                    file_size = os.path.getsize(sChildPath)/1024 if os.path.exists(sChildPath) else 0   # 单位为kb
                    # 视频文件时长， 单位 秒
                    if file_type.endswith(self.movie_types):
                        file_time = VideoFileClip(sChildPath).duration
                    else:
                        file_time = 0
                    if sChildPath.startswith(self.file_data_list[0]):
                        print(sChildPath)
                        print(self.file_data_list[0])
                        print(len(self.file_data_list[0]) - 1)
                        file_path = sChildPath[len(self.file_data_list[0]) +1:]
                        print(file_path)
                        db = 0
                    elif sChildPath.startswith(self.file_data_list[1]):
                        file_path = sChildPath[len(self.file_data_list[1]) +1:]
                        db = 1
                    elif sChildPath.startswith(self.file_data_list[2]):
                        file_path = sChildPath[len(self.file_data_list[2]) +1:]
                        db = 2
                    elif sChildPath.startswith(self.file_data_list[3]):
                        file_path = sChildPath[len(self.file_data_list[3]) +1:]
                        db = 3
                    elif sChildPath.startswith(self.file_data_list[4]):
                        file_path = sChildPath[len(self.file_data_list[4]) +1:]
                        db = 4
                    if self.f_data:
                        if self.f_data.get(sChildPath, None):
                            pass
                        else:
                            self.f_data[sChildPath] = 1
                            data_dict['file_name'] = file_name
                            data_dict['file_type'] = file_type[1:]
                            data_dict['file_size'] = file_size
                            data_dict['file_time'] = file_time
                            data_dict['file_path'] = file_path
                            data_dict['file_create_time'] = file_create_time
                            data_dict['file_update_time'] = file_update_time
                            data_dict['is_delete'] = 0
                            data_dict['label'] = ''
                            # self.create_data(data_dict, db)
                    else:
                        self.f_data[sChildPath] = 1
                        data_dict['file_name'] = file_name
                        data_dict['file_type'] = file_type[1:]
                        data_dict['file_size'] = file_size
                        data_dict['file_time'] = file_time
                        data_dict['file_path'] = file_path
                        data_dict['file_create_time'] = file_create_time
                        data_dict['file_update_time'] = file_update_time
                        data_dict['is_delete'] = 0
                        data_dict['file_label'] = 0
                        
                        # self.create_data(data_dict, db)
                
                    
                    # print(data_dict)
                    #判断当前遍历到的是文件还是文件夹.
                    if os.path.exists(sChildPath) and os.path.isdir(sChildPath):
                        #再次递归调用
                        print_dir_constents(sChildPath)
                    # print(data_dict)
                    # print(self.f_data)
            except FileNotFoundError as e:
                print(e)
                return
            finally:
                return
        print_dir_constents(self.path)
    def create_data(self, data, db):
        # 判断要添加到那个数据库中去
        
        print(db)
        # if db==0:
        #     new_data = FileData_000000()
        # elif db==1:
        #     new_data = FileDataDriving()
        # elif db==2:
        #     new_data = FileDataParking()
        # elif db==3:
        #     new_data = FileDataRadar()
        # elif db==4:
        #     new_data = FileDataVideo()
        # file_type = FileType.objectes.filter(file_type=data['file_type']).first()
        # if file_type:
        #     data['file_type'] = file_type['id']
        # else:
        #     file_type = FileType()
        #     file_type['file_type'] = data['file_type']
        #     file_type.save()
        #     data['file_type'] = FileType.objectes.filter(file_type=data['file_type']).first()['id']
        # new_data.file_name = data['file_name']
        # new_data.file_type = data['file_type']
        # new_data.file_size = data['file_size']
        # new_data.file_time = data['file_time']
        # new_data.file_path = data['file_path']
        # new_data.file_create_time = data['file_create_time']
        # new_data.file_update_time = data['file_update_time']
        # new_data.is_delete = data['is_delete']
        # new_data.is_delete = data['is_delete']
        # new_data.save()
    def __del__(self):
        self.f.close()
'''
import redis, time
class RefreshData:
    def __init__(self):
        
        self.r = redis.Redis()
        self.path = r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA'
        self.movie_types = (
            '.mp4', 
            '.mkv', 
            '.avi', 
            # '.wmv', 
            '.iso')
        
        self.FileData_000000 = []
        self.FileDataDriving = []
        self.FileDataParking = []
        self.FileDataRadar = []
        self.FileDataVideo = []
        # self.data_000000_file = open('./data_000000_file.json', 'w')
        # self.data_driving_file = open('./data_driving_file.json', 'w')
        # self.data_parking_file = open('./data_parking_file.json', 'w')
        self.data_radar_file = open('./data_radar_file.json', 'w')
        self.data_video_file = open('./data_video_file.json', 'w')
        # 记录起始时间
        self.file_list = [
            # self.data_000000_file,
            # self.data_driving_file,
            # self.data_parking_file,
            self.data_radar_file,
            self.data_video_file
        ]
        self.data_list = [
            # self.FileData_000000,
            # self.FileDataDriving,
            # self.FileDataParking,
            self.FileDataRadar,
            self.FileDataVideo,
        ]
        self.start_time = time.time()
        print('ザ・ワールド ，時を止まれ !!!')
        # 起始路径列表
        self.file_data_list = [
            # r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\000000', 
            # r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Driving', 
            # r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Parking', 
            r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Radar',
            r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Video']
        self.get_dirs_data()
        # self.write_data()
    # 查看存过没有
    def exit(self, key, value):
        return self.r.sismember(key, value)
    def get_dirs_data(self):
        def print_dir_constents(dir_path):
            try:
                for schild in os.listdir(dir_path):
                    if self.exit('file_path', schild):
                        print('重复数据丢弃')
                        continue
                    #拼接地址
                    data_dict = {}
                    sChildPath = os.path.normpath("{}\{}".format(dir_path, schild))
                    # print(sChildPath)
                    # print(sChildPath)
                    # 文件创建时间
                    file_create_time = time.localtime(os.path.getctime(sChildPath)) if os.path.exists(sChildPath) else '0-0-0-0-0-0'
                    if type(file_create_time) == str:
                        print('未获取到文件创建时间')
                    else:
                        # print(file_create_time)
                        file_create_time = str(file_create_time.tm_year) + '-' + str(file_create_time.tm_mon) + '-' + str(file_create_time.tm_mday) + '-' + str(file_create_time.tm_hour) + '-' + str(file_create_time.tm_min) + '-' + str(file_create_time.tm_sec)
                    # 文件修改时间
                    # print(file_create_time)
                    file_update_time = time.localtime(os.path.getmtime(sChildPath)) if os.path.exists(sChildPath) else '0-0-0-0-0-0'
                    if type(file_update_time) == str:
                        print('未获取到文件修改时间')
                    else:
                        # print(file_update_time)
                        file_update_time = str(file_update_time.tm_year) + '-' + str(file_update_time.tm_mon) + '-' + str(file_update_time.tm_mday) + '-' + str(file_update_time.tm_hour) + '-' + str(file_update_time.tm_min) + '-' + str(file_update_time.tm_sec)
                    # 文件类型和文件名
                    files=os.path.splitext(sChildPath)
                    file_name,file_type=files
                    # 文件名
                    file_name = file_name.split('\\')[-1]
                    # 文件类型
                    file_type = file_type if file_type else 'File folder'
                    # 文件大小
                    file_size = os.path.getsize(sChildPath)/1024 if os.path.exists(sChildPath) else 0   # 单位为kb
                    # 视频文件时长， 单位 秒
                    if file_type.endswith(self.movie_types):
                        file_time = VideoFileClip(sChildPath).duration
                    else:
                        file_time = 0
                    if sChildPath.startswith(self.file_data_list[0]):
                        # print(sChildPath)
                        # print(self.file_data_list[0])
                        # print(len(self.file_data_list[0]) - 1)
                        file_path = sChildPath[len(self.file_data_list[0]) +1:]
                        # print(file_path)
                        db = 0
                    elif sChildPath.startswith(self.file_data_list[1]):
                        file_path = sChildPath[len(self.file_data_list[1]) +1:]
                        db = 1
                    elif sChildPath.startswith(self.file_data_list[2]):
                        file_path = sChildPath[len(self.file_data_list[2]) +1:]
                        db = 2
                    elif sChildPath.startswith(self.file_data_list[3]):
                        file_path = sChildPath[len(self.file_data_list[3]) +1:]
                        db = 3
                    elif sChildPath.startswith(self.file_data_list[4]):
                        file_path = sChildPath[len(self.file_data_list[4]) +1:]
                        db = 4
                    self.r.sadd('file_path', schild)
                    data_dict['file_name'] = file_name
                    data_dict['file_type'] = file_type[1:]
                    data_dict['file_size'] = file_size
                    data_dict['file_time'] = file_time
                    data_dict['file_path'] = file_path
                    data_dict['file_create_time'] = file_create_time
                    data_dict['file_update_time'] = file_update_time
                    data_dict['is_delete'] = 0
                    data_dict['label'] = ''
                    self.create_data(data_dict, db)
                    #判断当前遍历到的是文件还是文件夹.
                    now_time = time.time() - self.start_time
                    print("{}秒过去了".format(now_time))
                    if os.path.exists(sChildPath) and os.path.isdir(sChildPath):
                        print_dir_constents(sChildPath)
            except FileNotFoundError as e:
                print(e)
                return
            finally:
                return
        for index,dir_path in enumerate(self.file_data_list):
            print_dir_constents(dir_path)
            print(self.data_list[index])
            print(self.file_list[index])
            json.dump(self.data_list[index],self.file_list[index])
            self.file_list[index].close()

    def create_data(self, data, db):
        if db==0:
            self.FileData_000000.append(data)
        elif db==1:
            self.FileDataDriving.append(data)
        elif db==2:
            self.FileDataParking.append(data)
        elif db==3:
            self.FileDataRadar.append(data)
        elif db==4:
            self.FileDataVideo.append(data)
    # def write_data(self):
        # json.dump(self.FileData_000000,self.data_000000_file)
        # json.dump(self.FileDataDriving,self.data_driving_file)
        # json.dump(self.FileDataParking,self.data_parking_file)
        # json.dump(self.FileDataRadar,self.data_radar_file)
        # json.dump(self.FileDataVideo,self.data_video_file)
    def __del__(self):
        self.data_000000_file.close()
        self.data_driving_file.close()
        self.data_parking_file.close()
        self.data_radar_file.close()
        self.data_video_file.close()
if __name__ == "__main__":
    ref = RefreshData()
