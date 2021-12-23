import RPi.GPIO as GPIO
import time
import cv2
from lcd import drivers

TRIG_PIN = 27 # GPIO 출력 Pin(초음파 센서)
ECHO_PIN = 22 # GPIO 입력 Pin (초음파 센서)

SWITCH_PIN = 12 # 스위치 Pin

# GPIO 7개 Pin 번호 설정
#                A   B   C   D   E  F  G
SEGMENT_PINS = [20, 21, 26, 19, 13, 7, 8] # 7 segment Pin

data = [0, 1, 1, 0, 0, 0, 0] # 1

GPIO.setmode(GPIO.BCM) # GPIO 초기설정
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # 풀다운저항
GPIO.setup(SWITCH_PIN, GPIO.OUT)

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

display = drivers.Lcd() 

cap = cv2.VideoCapture(0) # 카메라 장치 열기

if not cap.isOpened():
    print('Camera open failed')
    exit()

def lcd(): # lcd 출력 함수
    display.lcd_display_string("   !!human!!", 1) # !!human!! 출력

try:
    while True:
        ret, img = cap.read() 
        if not ret:
            break

        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001) # 10us (microsec)
        GPIO.output(TRIG_PIN, False)
        switch = GPIO.input(SWITCH_PIN)
        while GPIO.input(ECHO_PIN) == 0: # 펄스 발생 중
            pass
        start = time.time() # ECHO PIN HIGH (시작)

        while GPIO.input(ECHO_PIN) == 1: # 펄스 발생 종료
            pass
        stop = time.time() # ECHO PIN LOW (종료)

        duration_time = stop - start
        distance = duration_time * 17160 # 34321/2

        if distance <= 20: # 20cm 안으로 감지되면
            for _ in range(3):
                for i in range(len(SEGMENT_PINS)):
                    GPIO.output(SEGMENT_PINS[i], data[i])

                time.sleep(0.5)

                for i in range(len(SEGMENT_PINS)):
                    GPIO.output(SEGMENT_PINS[i], GPIO.LOW)
                        
                time.sleep(0.5)

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        # xml 분류기 파일 로그
        face_cascade = cv2.CascadeClassifier('./xml/face.xml')
        eye_cascade = cv2.CascadeClassifier('./xml/eye.xml')

        faces = face_cascade.detectMultiScale(gray) # 얼굴 검출
        
        # 얼굴 위치에 대한 좌표 정보 가져오기
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

            # 얼굴이 검출된 영역 내부에서만 진행하기 위해 ROI 생성
            roi_gray = gray[y:y+h, x:x+w] 
            roi_color = img[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray) # 눈 검출
            
            # 눈 위치에 대한 좌표 정보 가져오기
            for(ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
            lcd() # 함수 실행
        
        cv2.imshow('camera',img) # 현재 프레임 영상 출력

        if cv2.waitKey(10) == 32:
            break
            
        if(switch == 1): # 스위치를 누르면
            display.lcd_clear() # lcd 출력 clear
            cv2.destroyAllWindows() # 열려있는 모든 창 닫기
            cap.release() # 사용자 자원 해제
            GPIO.cleanup() # GPIO 리소스 해제
            break
finally:
    print('exit')