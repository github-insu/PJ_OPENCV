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


#############################################################
# 첫 페이지 #################################################
#############################################################
def Home(request):
    return render(request, 'home.html')


#############################################################
# Service 1 : 이미지 색상변환 ################################
#############################################################
def ViewImage(request):
    if request.method == 'POST':

        # 파일명, byte_img.read()-바이트열
        byte_img = request.FILES['file_image']

        img_rgb = cv2.imdecode(np.fromstring(byte_img.read(), np.uint8), cv2.IMREAD_COLOR)
        
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

        img = cv2.GaussianBlur(img_gray, (5,5), 0)
        img_th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)
        
        # img 파일을 jpg형식으로 인코딩한 numpy array로 변환 #
        _, en_img_rgb = cv2.imencode('.jpg', img_rgb)
        _, en_img_gray = cv2.imencode('.jpg', img_gray)
        _, en_img_th = cv2.imencode('.jpg', img_th)
        
        # 인코딩한 객체를 바이트화 #
        byte_img_rgb = en_img_rgb.tobytes()
        byte_img_gray = en_img_gray.tobytes()
        byte_img_th = en_img_th.tobytes()

        # 바이트화한 객체를 전송하기 알맞은 형태로 가공 #
        base64_img_rgb = base64.b64encode(byte_img_rgb).decode('utf-8')
        base64_img_gray = base64.b64encode(byte_img_gray).decode('utf-8')
        base64_img_th = base64.b64encode(byte_img_th).decode('utf-8')

        context = {'img_rgb' : base64_img_rgb, 'img_gray' : base64_img_gray, 'img_th' : base64_img_th}

        return render(request, 'index.html', context)
    else :
        return render(request, 'index.html')
    
############################################################
# Service 2 : 객체 추적 ##############################
############################################################

def LoadVideo(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file_video']
        context = {'file' : uploaded_file}
        return context
    return render(request, 'objectdetect.html')

# 비디오 스트리밍
def video_stream(request):
    print('point1')
    byte_videos = LoadVideo(request)['file']
    print('point2')
    for byte_video in byte_videos:
        encoded_byte_video = np.fromstring(byte_video, dtype=np.uint8)
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_byte_video) + b'\r\n')

    # cap = cv2.VideoCapture('./notify/templates/images/walking_human.mp4')
    # while cap.isOpened():
    #     ret, frame = cap.read()

    #     if not ret:
    #         break

    #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #     _, frame_encoded = cv2.imencode('.jpg', frame)
    #     yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame_encoded) + b'\r\n')
    

def ObjectDetect(request):    
    return StreamingHttpResponse(video_stream(request), content_type='multipart/x-mixed-replace; boundary=frame')