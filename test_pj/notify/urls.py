from django.urls import path
from . import views
from .views import Home

urlpatterns = [
    # 첫 페이지
    path('', views.Home),

    # 이미지 처리
    path('image/', views.loadImage),
    path('image/view/', views.ViewImage),
]