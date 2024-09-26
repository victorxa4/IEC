from django.urls import path
from .views import *

urlpatterns = [
    path('read_img/', Read_Image_View.as_view(), name='read_img'),
]
