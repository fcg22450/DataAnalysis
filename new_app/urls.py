from django.urls import path, re_path, include
from .views import *
urlpatterns = [
    # 数据获取接口
    path('getbase/', BaseFileGet.as_view({
        'get': 'list'
    })),
    # 获取标签接口
    path('getlabels/', GetLabel.as_view({
        'get': 'list'
    })),
    # 创建标签接口
    path('createlabel/', LabelClass.as_view()),
    # path('disk_scan/', RefreshData.as_view())
    path('get_data_size/', DataFileSizes.as_view()),
    path('get_data_sum/', DataFileNum.as_view()),
    # 获取所有文件信息, 同时作为搜索接口来进行使用
    path('get_file_data/', FileDataGet.as_view()),
    path('create_db_data/', create_db_data),
    path('file_type_list/', FileTypeGet.as_view({
        'get': 'list'
    })),
    path('create_db_from_base/', create_db_from_base),
    path('get_base_file_data/', GetBaseFileSize.as_view()),
    path('update_label/', UpdateLabel.as_view())
]
