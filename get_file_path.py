# path1 = r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA'
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
# file_data_list = ['\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\000000', '\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Driving', '\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Parking', '\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Radar', '\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Video']
# movie_types = ('.mp4', '.mkv', '.avi', '.wmv', '.iso')
# def print_dir_constents(path1):
#     for schild in os.listdir(path1):
#                 #拼接地址
#         sChildPath = os.path.join(path1, schild)
#         # 文件创建时间
#         create_time = time.localtime(os.path.getctime(sChildPath))
#         # 文件修改时间
#         update_time = time.localtime(os.path.getmtime(sChildPath))
#         # 文件类型和文件名
#         files=os.path.splitext(sChildPath)
#         filename,file_type=files
#         # 文件名
#         filename = filename.split('\\')[-1]
#         # 文件类型
#         file_type = file_type if file_type else 'File folder'
#         # 文件大小
#         file_size = os.path.getsize(sChildPath)/1024   # 单位为kb
#         # 视频文件时长， 单位 秒
#         if file_type.endswith(movie_types):
#             file_time = VideoFileClip(sChildPath).duration
#         else:
#             file_time = 0
#         #判断当前遍历到的是文件还是文件夹
#         if os.path.isdir(sChildPath):
#             #再次递归调用
#             print_dir_constents(sChildPath)


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
        self.movie_types = ('.mp4', '.mkv', '.avi', '.wmv', '.iso')
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
            for schild in os.listdir(dir_path):
                
                #拼接地址
                data_dict = {}
                sChildPath = os.path.join(dir_path, schild)
                # print(sChildPath)
                # 文件创建时间
                file_create_time = time.localtime(os.path.getctime(sChildPath)) if os.path.exists(sChildPath) else '0-0-0-0-0-0'
                if type(file_create_time) == str:
                    pass
                else:
                    print(file_create_time)
                    file_create_time = str(file_create_time.tm_year) + '-' + str(file_create_time.tm_mon) + '-' + str(file_create_time.tm_mday) + '-' + str(file_create_time.tm_hour) + '-' + str(file_create_time.tm_min) + '-' + str(file_create_time.tm_sec)
                # 文件修改时间
                # print(file_create_time)
                file_update_time = time.localtime(os.path.getmtime(sChildPath)) if os.path.exists(sChildPath) else '0-0-0-0-0-0'
                if file_update_time is str:
                    pass
                else:
                    print(file_update_time)
                    file_update_time = str(file_update_time.tm_year) + '-' + str(file_update_time.tm_mon) + '-' + str(file_update_time.tm_mday) + '-' + str(file_update_time.tm_hour) + '-' + str(file_update_time.tm_min) + '-' + str(file_update_time.tm_sec)
                # 文件类型和文件名
                files=os.path.splitext(sChildPath)
                file_name,file_type=files
                # 文件名
                file_name = file_name.split('\\')[-1]
                # 文件类型
                file_type = file_type if file_type else 'File folder'
                # 文件大小
                file_size = os.path.getsize(sChildPath)/1024   # 单位为kb
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
                    data_dict['label'] = ''
                    
                    # self.create_data(data_dict, db)
            
                
                # print(data_dict)
                #判断当前遍历到的是文件还是文件夹.
                if os.path.isdir(sChildPath):
                    #再次递归调用
                    print_dir_constents(sChildPath)
                # print(data_dict)
                # print(self.f_data)
        print_dir_constents(self.path)
    def create_data(self, data, db):
        # 判断要添加到那个数据库中去
        
        print(db)
        # if db==0:
        #     pass
        # elif db==1:
        #     pass
        # elif db==2:
        #     pass
        # elif db==3:
        #     pass
        # elif db==4:
        #     pass
    def __del__(self):
        self.f.close()

if __name__ == "__main__":
    ref = RefreshData()
