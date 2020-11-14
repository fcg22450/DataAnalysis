from rest_framework import serializers

from .models import FileData_000000,FileDataDriving,FileDataParking,FileDataRadar,FileDataVideo,FileType,BaseFilePath,Labels


class FileData_000000Serializers(serializers.Serializer):
    
    class Meta:
        model = FileData_000000
        fields = '__all__'
class FileDataDrivingSerializers(serializers.Serializer):
    class Meta:
        model = FileDataDriving
        fields = '__all__'
class FileDataParkingSerializers(serializers.Serializer):
    class Meta:
        model = FileDataParking
        fields = '__all__'
class FileDataRadarSerializers(serializers.Serializer):
    class Meta:
        model = FileDataRadar
        fields = '__all__'
class FileDataVideoSerializers(serializers.Serializer):
    class Meta:
        model = FileDataVideo
        fields = '__all__'
class FileTypeSerializers(serializers.Serializer):
    class Meta:
        model = FileType
        fields = '__all__'
class BaseFilePathSerializers(serializers.Serializer):
    class Meta:
        model = BaseFilePath
        fields = '__all__'
class LabelsSerializers(serializers.Serializer):
    class Meta:
        model = Labels
        fields = '__all__'