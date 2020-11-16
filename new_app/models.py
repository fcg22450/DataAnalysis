from django.db import models

# Create your models here.
class Base(models.Model):
    # 删除情况
    is_delete = models.IntegerField(default=0)  # 是否删除：默认0：未删除，1：已删除

    class Meta:
        abstract = True

class BaseFilePath(Base):
    # 基础盘的名字
    file_name = models.CharField(max_length=200)
    # 基础盘的路径
    file_path = models.TextField()
    # 基础盘对应的数据库模型类的名字
    table_name = models.CharField(max_length=200)

    class Meta:
        db_table = 'base_file_path'
        
class FileData_000000(Base):
    file_name = models.TextField()
    file_type = models.IntegerField()
    file_size = models.IntegerField()
    file_path = models.TextField()
    file_create_time = models.CharField(max_length=200)
    file_update_time = models.CharField(max_length=200)
    file_video_length = models.CharField(max_length=200)
    file_label = models.CharField(max_length=200)

    class Meta:
        db_table = 'file_data_000000'
        # ununique_together = ('file_path',)

class FileDataDriving(Base):
    file_name = models.TextField()
    file_type = models.IntegerField()
    file_size = models.IntegerField()
    file_path = models.TextField()
    file_create_time = models.CharField(max_length=200)
    file_update_time = models.CharField(max_length=200)
    file_video_length = models.CharField(max_length=200)
    file_label = models.CharField(max_length=200)

    class Meta:
        db_table = 'file_data_driving'
        # ununique_together = ('file_path',)

class FileDataParking(Base):
    file_name = models.TextField()
    file_type = models.IntegerField()
    file_size = models.IntegerField()
    file_path = models.TextField()
    file_create_time = models.CharField(max_length=200)
    file_update_time = models.CharField(max_length=200)
    file_video_length = models.CharField(max_length=200)
    file_label = models.CharField(max_length=200)

    class Meta:
        db_table = 'file_data_parking'
        # ununique_together = ('file_path',)

class FileDataRadar(Base):
    file_name = models.TextField()
    file_type = models.IntegerField()
    file_size = models.IntegerField()
    file_path = models.TextField()
    file_create_time = models.CharField(max_length=200)
    file_update_time = models.CharField(max_length=200)
    file_video_length = models.CharField(max_length=200)
    file_label = models.CharField(max_length=200)

    class Meta:
        db_table = 'file_data_radar'
        # ununique_together = ('file_path',)

class FileDataVideo(Base):
    file_name = models.TextField()
    file_type = models.IntegerField()
    file_size = models.IntegerField()
    file_path = models.TextField()
    file_create_time = models.CharField(max_length=200)
    file_update_time = models.CharField(max_length=200)
    file_video_length = models.CharField(max_length=200)
    file_label = models.CharField(max_length=200)

    class Meta:
        db_table = 'file_data_video'
        # ununique_together = ('file_path',)

class FileType(Base):
    file_type = models.TextField()
    class Meta:
        db_table = 'file_type'

class Labels(Base):
    label = models.TextField()

    class Meta:
        db_table = 'labels'