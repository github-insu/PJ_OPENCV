#########################라이브러리 ###########################
# django 라이브러리
from django.shortcuts import render,HttpResponse

# 이미지 처리 라이브러리
import numpy as np
import math
import cv2
import base64

# 비디오 스트리밍 라이브러리
from django.http import StreamingHttpResponse

# #로그 기록 관련 라이브러리
# import logging




#############################################################
# 로그 기록 #################################################
#############################################################

# # 로거 인스턴스
# logger = logging.getLogger(__name__)

# def my_view(request, arg1, arg2):
#     # debug레벨 이상의 로그 레코드를 기록
#     logger.debug('arg1: %s, arg2: %s', arg1, arg2)


#############################################################
# 첫 페이지 #################################################
#############################################################
def Home(request):
    return render(request, 'home.html')

############################################################
# 함수 #####################################################
############################################################

# 이미지 로드(찾은 파일 형식 : 바이트객체)
def loadImage(request):
    byte_img = request.FILES['file_image']
    print(byte_img)
    context = {'img_data' : byte_img}
    print(context)
    return context


# 이미지 디코딩(바이트 객체 -> bgr객체)
def decodeImage(request):
    byte_img = loadImage(request)['img_data']
    img_bgr = cv2.imdecode(np.fromstring(byte_img.read(), np.uint8), cv2.IMREAD_COLOR)
    context = {'img_data' : img_bgr}
    return context

# 이미지 인코딩(바이트 객체 -> base64)
def viewImage(request):
    byte_img = loadImage(request)['img_data']
    base64_img = base64.b64encode(byte_img.read()).decode('utf-8')
    context = {'img_data' : base64_img}
    return context


#############################################################
# Service 0 : 이미지 불러오기 ################################
#############################################################
# 이미지 불러오기(바이트객체 -> base64인코딩)
def ViewImage(request):
    if request.method == 'POST':
        context = viewImage(request)
        return render(request, 'index.html', context)
    else :
        return render(request, 'index.html')