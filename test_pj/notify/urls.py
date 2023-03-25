from django.urls import path
from . import views
from .views import Home

urlpatterns = [
    # 첫 페이지
    path('', views.Home),

    # 이미지 처리
    path('image/view/', views.ViewImage),

    # 영상 처리
    path('video/filevideo/', views.LoadVideo, name="LoadVideo"),
    path('video/object_detect/', views.ObjectDetect, name="object_detect"),
]