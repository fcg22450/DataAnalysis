import os,time,json
# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# from django.db.models import Q
from .models import FileData_000000,FileDataDriving,FileDataParking,FileDataRadar,FileDataVideo,FileType,BaseFilePath
from .serializers import FileData_000000Serializers,FileDataDrivingSerializers,FileDataParkingSerializers,FileDataRadarSerializers,FileDataVideoSerializers,FileTypeSerializers,BaseFilePathSerializers

# 获取文件时长的模块
from moviepy.editor import VideoFileClip
# 基础盘信息获取接口
class BaseFileGet(ModelViewSet):
    queryset = BaseFilePath.objects.all()
    serializer_class = BaseFilePathSerializers
    
# 搜索功能对应接口
class FileDataGet(APIView):
    def get(self, request):
        # 要搜索的文件名   单字符串
        search_name = request.GET.get('search_name', None)
        # 选定的文件类型   元组转列表
        file_type = list(request.GET.get('file_type', None))
        # 选定的文件大小的范围   元组转列表
        min_file_size, max_file_size = list(request.GET.get('file_size', None))
        # 选定的搜索范围   元组形式
        file_path = tuple(request.GET.get('file_path', None))
        # 获取到要进行搜索的表名
        search_table = []
        if file_path:
            for path in file_path:
                table_name = BaseFilePath.objects.filter(file_name=path).first()['table_name']
                search_table.append(table_name)
        else:
            search_table = [x['table_name'] for x in BaseFilePath.objects.all()]
        
        conditions = {}
        if search_name:
            conditions['file_name'] = search_name
        if file_type:
            conditions['file_type__in'] = file_type
        if min_file_size and max_file_size:
            conditions['file_type__gte'] = min_file_size
            conditions['file_type__lte'] = max_file_size
        data_list = []
        for table in search_table:
        # 判断是否限定文件大小
        # 判断是否限定文件类型
            file_data_list = eval(table).objects.filter(**conditions)
            file_data_list = eval(table+'Serializers')(file_data_list, many=True)
            data_list += file_data_list
        # 判断是否有输入名字
        return Response({"code":200, 'message':'请求成功', 'data':data_list})
        

'''
class RefreshData:
    def __init__(self):
        if os.path.exists('./data_fingerprint_file.json'):
            self.f = open('./data_fingerprint_file.json', 'r', encoding='urf-8')
            self.f_data = json.load(self.f)
        else:
            self.f = open('./data_fingerprint_file.json', 'w', encoding='urf-8')
        self.path = r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA'
        self.dir_path = ('.mp4', '.mkv', '.avi', '.wmv', '.iso')
        self.file_data_list = [
            r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\000000', 
            r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Driving', 
            r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Parking', 
            r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Radar', 
            r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Video']
        self.get_dirs_data()
        
    def get_dirs_data(self):
        def print_dir_constents(dir_path):
            for schild in os.listdir(dir_path):
                #拼接地址
                data_dict = {}
                sChildPath = os.path.join(dir_path, schild)
                # 文件创建时间
                file_create_time = time.localtime(os.path.getctime(sChildPath))
                # 文件修改时间
                file_update_time = time.localtime(os.path.getmtime(sChildPath))
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
                    db = 0
                elif sChildPath.startswith(self.file_data_list[1]):
                    db = 1
                elif sChildPath.startswith(self.file_data_list[1]):
                    db = 2
                elif sChildPath.startswith(self.file_data_list[1]):
                    db = 3
                elif sChildPath.startswith(self.file_data_list[1]):
                    db = 4
                if self.f_data:
                    if self.f_data.get(sChildPath, default=None):
                        continue
                    else:
                        self.f_data[sChildPath] = 1
                data_dict['file_name'] = file_name
                data_dict['file_type'] = file_type
                data_dict['file_size'] = file_size
                data_dict['file_time'] = file_time
                data_dict['file_path'] = sChildPath
                data_dict['file_create_time'] = file_create_time
                data_dict['file_update_time'] = file_update_time
                data_dict['is_delete'] = 0
                #判断当前遍历到的是文件还是文件夹
                self.create_data(data_dict, db)
                if os.path.isdir(sChildPath):
                    #再次递归调用
                    print_dir_constents(sChildPath)
        print_dir_constents(self.path)
    def create_data(self, data, db):
        # 判断要添加到那个数据库中去
        
        print(db)
        if db==0:
            pass
        elif db==1:
            pass
        elif db==2:
            pass
        elif db==3:
            pass
        elif db==4:
            pass
    def __del__(self):
        with open('./data_fingerprint_file.json', 'w', encoding='urf-8') as f:
            json.dump(self.f_data, f)
        self.f.close()


'''