import os,time,json, redis
# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import FileData_000000,FileDataDriving,FileDataParking,FileDataRadar,FileDataVideo,FileType,BaseFilePath,Labels
from .serializers import FileData_000000Serializers,FileDataDrivingSerializers,FileDataParkingSerializers,FileDataRadarSerializers,FileDataVideoSerializers,FileTypeSerializers,BaseFilePathSerializers,LabelsSerializers

# 获取文件时长的模块
from moviepy.editor import VideoFileClip

# 基础盘信息获取接口
class BaseFileGet(ModelViewSet):
    queryset = BaseFilePath.objects.all()
    serializer_class = BaseFilePathSerializers

    def list(self, request, *args, **kwargs):
        queryset = BaseFilePath.objects.all()
        data_list = []
        for data in queryset:
            data_dict = {}
            data_dict['file_name'] = data.file_name
            data_dict['file_path'] = data.file_path
            data_dict['table_name'] = data.table_name
            data_list.append(data_dict)
        return Response({'code': 200, 'message': '基础盘信息获取成功','data': data_list})
    
# 搜索功能对应接口
class FileDataGet(APIView):
    def get(self, request):
        # 要搜索的文件名   单字符串
        data = json.loads(request.GET.get('data', None))
        search_name = data['search_name']
        # 选定的文件类型   元组转列表
        file_type = data['file_type']
        # 选定的文件大小的范围   元组转列表
        min_file_size, max_file_size = data['file_size']
        # 选定的搜索范围   元组形式
        file_path = data['file_path']
        # 获取到要进行搜索的表名
        search_table = []
        if file_path:
            for path in file_path:
                table_name = BaseFilePath.objects.filter(table_name=path).first().table_name
                search_table.append(table_name)
        else:
            search_table = [x['table_name'] for x in BaseFilePath.objects.all().values()]
        conditions = {}
        if search_name:
            conditions['file_name__icontains'] = search_name
        if file_type:
            conditions['file_type__in'] = file_type
        if min_file_size and max_file_size:
            conditions['file_type__gte'] = min_file_size
            conditions['file_type__lte'] = max_file_size
        data_list = []
        for table in search_table:
        # 判断是否限定文件大小
        # 判断是否限定文件类型
        # 获取对应基础盘路径
            base_file_path = BaseFilePath.objects.filter(table_name=table).first().file_path
            # print(table)
            # base_file_path = ''
            if conditions== []:
                file_data_list = eval(table).objects.all().values()
            else:
                file_data_list = eval(table).objects.filter(**conditions).values()
            new_data_list = []
            for file_data in file_data_list:
                file_data['db'] = table
                label_list = []
                for label in json.loads(file_data['file_label']):
                    label_name = Labels.objects.filter(id=label).first().label
                    label_list.append(label_name)
                file_data['file_label'] = ''.join(label_list)
                file_data['file_path'] = base_file_path + file_data['file_path']
                new_data_list.append(file_data)
            data_list.extend(new_data_list)
        return Response({"code":200, 'message':'请求成功', 'data':data_list})
# 标签创建接口
class LabelClass(APIView):
    def get(self, request):
        # 新建的标签的名称
        label_name = request.GET.get('label', None)
        db = request.GET.get('table', None)
        file_id = request.GET.get('id', None)
        res = {}
        labels = Labels.objects.filter(label=label_name).first()
        if labels:
            label_id = labels.id
        else:
            label = Labels()
            label.label = label_name
            label.save()
            label_id = Labels.objects.filter(label=label_name).first()
        file_data = eval(db).objects.filter(id=file_id).first()
        file_data.file_label = json.dumps(json.loads(file_data.file_label).append(label_id))
        file_data.save()
        res['code'] = 200
        res['message'] = '标签修改成功'
        return Response(res)
# 标签修改
class UpdateLabel(APIView):
    def get(self, request):
        new_label = request.GET.get('label', None).split(',')
        db = request.GET.get('table', None)
        file_id = request.GET.get('id', None)
        label_list = []
        for label in new_label:
            labels = Labels.objects.filter(label=label_name).first()
            if labels:
                label_id = labels.id
            else:
                label = Labels()
                label.label = label_name
                label.save()
                label_id = Labels.objects.filter(label=label_name).first()
            label_list.append(label_id)
        file_data = eval(db).objects.filter(id=file_id).first()
        file_data.file_label = json.dumps(label_list)
        res = {}
        res['code'] = 200
        res['message'] = '修改成功'
        return Response(res)
        
# 标签获取接口
class GetLabel(ModelViewSet):
    queryset = Labels.objects.all()
    serializer_class = LabelsSerializers
    def list(self, request, *args, **kwargs):
        queryset = Labels.objects.all()
        data_list = []
        for data in queryset:
            data_dict = {}
            data_dict['id'] = data.id
            data_dict['label'] = data.label
            data_list.append(data_dict)
        return Response({'code': 200, 'message': '文件类型信息获取成功','data': data_list})
class File_data_init:
    def __init__(self):
        self.file_data_000000 = FileData_000000.objects.values('file_type','file_size')
        self.file_data_driving = FileDataDriving.objects.values('file_type','file_size')
        self.file_data_parking = FileDataParking.objects.values('file_type','file_size')
        self.file_data_radar = FileDataRadar.objects.values('file_type','file_size')
        self.file_data_video = FileDataVideo.objects.values('file_type','file_size')
class GetBaseFileSize(APIView, File_data_init):
    def __init__(self):
        super().__init__()
    def get(self, request):
        # 获取文件分类
        file_type_list = FileType.objects.all()
        # 获取数据
        file_data_000000 = FileData_000000.objects.values('file_type','file_size')
        file_data_driving = FileDataDriving.objects.values('file_type','file_size')
        file_data_parking = FileDataParking.objects.values('file_type','file_size')
        file_data_radar = FileDataRadar.objects.values('file_type','file_size')
        file_data_video = FileDataVideo.objects.values('file_type','file_size')

        # file_data_000000_list = {i['file_type'] for i in file_data_000000}
        # file_data_driving_list = {i['file_type'] for i in file_data_driving}
        # file_data_parking_list = {i['file_type'] for i in file_data_parking}
        # file_data_radar_list = {i['file_type'] for i in file_data_radar}
        # file_data_video_list = {i['file_type'] for i in file_data_video}

        file_data_dict_000000 = {type_data.file_type:[] for type_data in file_type_list}
        file_data_dict_driving = {type_data.file_type:[] for type_data in file_type_list}
        file_data_dict_parking = {type_data.file_type:[] for type_data in file_type_list}
        file_data_dict_radar = {type_data.file_type:[] for type_data in file_type_list}
        file_data_dict_video = {type_data.file_type:[] for type_data in file_type_list}
        for data in file_data_000000:
            # 这个文件的类型
            this_file_type = FileType.objects.filter(id=data['file_type']).first().file_type
            file_data_dict_000000[this_file_type].append(data['file_size'])
        for data in file_data_driving:
            # 这个文件的类型
            this_file_type = FileType.objects.filter(id=data['file_type']).first().file_type
            file_data_dict_driving[this_file_type].append(data['file_size'])
        for data in file_data_parking:
            # 这个文件的类型
            this_file_type = FileType.objects.filter(id=data['file_type']).first().file_type
            file_data_dict_parking[this_file_type].append(data['file_size'])
        for data in file_data_radar:
            # 这个文件的类型
            this_file_type = FileType.objects.filter(id=data['file_type']).first().file_type
            file_data_dict_radar[this_file_type].append(data['file_size'])
        for data in file_data_video:
            # 这个文件的类型
            this_file_type = FileType.objects.filter(id=data['file_type']).first().file_type
            file_data_dict_video[this_file_type].append(data['file_size'])
        file_data_000000_sum = sum(FileData_000000.objects.values_list('file_size', flat=True))
        file_data_driving_sum = sum(FileDataDriving.objects.values_list('file_size', flat=True))
        file_data_parking_sum = sum(FileDataParking.objects.values_list('file_size', flat=True))
        file_data_radar_sum = sum(FileDataRadar.objects.values_list('file_size', flat=True))
        file_data_video_sum = sum(FileDataVideo.objects.values_list('file_size', flat=True))
        data = [
            [{'name': key,'value': sum(value)} for key,value in file_data_dict_000000.items() if sum(value) >= file_data_000000_sum/100 and file_data_000000_sum>0],
            [{'name': key,'value': sum(value)} for key,value in file_data_dict_driving.items() if sum(value) >= file_data_driving_sum/100 and file_data_driving_sum>0],
            [{'name': key,'value': sum(value)} for key,value in file_data_dict_parking.items() if sum(value) >= file_data_parking_sum/100 and file_data_parking_sum>0],
            [{'name': key,'value': sum(value)} for key,value in file_data_dict_radar.items() if sum(value) >= file_data_radar_sum/100 and file_data_radar_sum>0],
            [{'name': key,'value': sum(value)} for key,value in file_data_dict_video.items() if sum(value) >= file_data_video_sum/100 and file_data_video_sum>0],
        ]
        type_list = [type_data.file_type for type_data in file_type_list]
        return Response({'code': 200, 'message': '数据获取成功', 'data': data, 'type_list': type_list})
            
        
# 构建饼图需要的数据， 这里构建的数据为各个路径下的文件数量的对比
# 弃之不用
class DataFileNum(APIView):
    def get(self, request):
        file_data_000000 = len(FileData_000000.objects.all())
        file_data_driving = len(FileDataDriving.objects.all())
        file_data_parking = len(FileDataParking.objects.all())
        file_data_radar = len(FileDataRadar.objects.all())
        file_data_video = len(FileDataVideo.objects.all())
        data = [
            {'value': file_data_000000, 'name': '000000'},
            {'value': file_data_driving, 'name': 'driving'},
            {'value': file_data_parking, 'name': 'parking'},
            {'value': file_data_radar, 'name': 'radar'},
            {'value': file_data_video, 'name': 'video'}
            ]
        return Response({'code':200, 'message': '数据请求成功', 'data': data})
# 构建饼图需要的数据， 这里构架的数据为哥哥路径下的文件数量的大小
# 弃之不用
class DataFileSizes(APIView):
    def get(self, request):
        file_data_000000 = sum(FileData_000000.objects.values_list('file_size', flat=True))
        file_data_driving = sum(FileDataDriving.objects.values_list('file_size', flat=True))
        file_data_parking = sum(FileDataParking.objects.values_list('file_size', flat=True))
        file_data_radar = sum(FileDataRadar.objects.values_list('file_size', flat=True))
        file_data_video = sum(FileDataVideo.objects.values_list('file_size', flat=True))
        data = [
            {'value': file_data_000000, 'name': '000000'},
            {'value': file_data_driving, 'name': 'driving'},
            {'value': file_data_parking, 'name': 'parking'},
            {'value': file_data_radar, 'name': 'radar'},
            {'value': file_data_video, 'name': 'video'}
            ]
        return Response({'code':200, 'message': '数据请求成功', 'data': data})
# 获取文件类型列表
class FileTypeGet(ModelViewSet):
    queryset = FileType.objects.all()
    serializer_class = FileTypeSerializers
    def list(self, request, *args, **kwargs):
        queryset = FileType.objects.all()
        data_list = []
        for data in queryset:
            data_dict = {}
            data_dict['id'] = data.id
            data_dict['file_type'] = data.file_type
            data_list.append(data_dict)
        return Response({'code': 200, 'message': '文件类型信息获取成功','data': data_list})
# 基础盘信息添加模块
def create_db_from_base(request):
    base_list = [
        {'file_name': '000000', 'file_path': r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\000000', 'table_name': 'FileData_000000'},
        {'file_name': 'Driving', 'file_path': r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Driving', 'table_name': 'FileDataDriving'},
        {'file_name': 'Parking', 'file_path': r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Parking', 'table_name': 'FileDataParking'},
        {'file_name': 'Radar', 'file_path': r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Radar', 'table_name': 'FileDataRadar'},
        {'file_name': 'Video', 'file_path': r'\\abtvdfs2.de.bosch.com\ismdfs\loc\szh\DA\Video', 'table_name': 'FileDataVideo'},
    ]
    for base in base_list:
        new_base = BaseFilePath()
        new_base.file_name = base['file_name']
        new_base.file_path = base['file_path']
        new_base.table_name = base['table_name']
        new_base.save()
    # return Response({'code': 200, 'message': '基础盘数据存储完成'})
'''
硬盘扫描模块
原定扫描模块因为ubuntu自动编译路径导致无法使用，所以改成在外部运行模块， 然后存储到json文件中去， 最后将json文件传输到服务器中进行读取
然后再由写好的定时任务读取这些json文件来存储到数据库中
真是有够绕的
'''
def create_db_data(request):
    db_table_list = [
        FileData_000000,
        FileDataDriving,
        FileDataParking,
        # FileDataRadar,
        # FileDataVideo()
    ]
    db_create = Data_create_db()
    for index,db in enumerate(db_table_list):
        db_create.data_save(db,index)
    return Response({'code':200, 'message': '数据追加完成'})
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
            db_con = db()
            db_con.file_name = data['file_name']
            file_type = FileType.objects.filter(file_type=data['file_type']).first()
            if file_type:
                db_con.file_type = file_type.id
            else:
                new_file_type = FileType()
                new_file_type.file_type = data['file_type']
                new_file_type.save()
                file_type = FileType.objects.filter(file_type=data['file_type']).first()
                db_con.file_type = file_type.id
            db_con.file_size = data['file_size']
            db_con.file_time = data['file_time']
            db_con.file_path = data['file_path']
            db_con.file_create_time = data['file_create_time']
            db_con.file_update_time = data['file_update_time']
            db_con.is_delete = data['is_delete']
            db_con.is_delete = data['is_delete']
            db_con.save()
        print(db)

    def __del__(self):
        self.data_000000_file.close()
        self.data_driving_file.close()
        self.data_parking_file.close()
        self.data_radar_file.close()
        self.data_video_file.close()

