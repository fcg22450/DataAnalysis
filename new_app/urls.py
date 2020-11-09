from django.urls import path, re_path, include
from .views import *
urlpatterns = [
    path('getbase/', BaseFileGet.as_view({
        'get': 'list'
    }))
]
