import RPi.GPIO as GPIO
import time

SW=[5, 6, 13, 19] # 스위치 1, 2, 3, 4
swValue=[0, 0, 0, 0] # 현재 스위치 입력 상태
swOldValue=[0, 0, 0, 0] # 과거 스위치 입력 상태
num=[0, 0, 0, 0] # 각 스위치 누른 횟수

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in range(len(SW)):
    GPIO.setup(SW[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        for i in range(len(SW)):
            swValue[i]=GPIO.input(SW[i])
        for i in range(len(SW)):
            if(swValue[i]==1 and swOldValue[i]==0): # 스위치가 현재 눌려있을 때
                num[i]+=1 # 누적 횟수 1 증가 후 아래 문자열 출력
                print('SW%d click'%(i+1), num[i])
                swOldValue[i]=swValue[i] # 현재 스위치 상태를 이전 스위치 상태로
                if(swOldValue[i]==1): # 이전 스위치 상태가 1일 때
                    continue # 그대로 넘어가기
            if(swOldValue[i]==1 and swValue[i]==0): # 이전 스위치 상태 1이고 현재 스위치 상태 0일 때=누르고 있지 않을 때
                swOldValue[i]=swValue[i] # 현재 스위치 상태를 이전 스위치 상태로
        time.sleep(0.1)
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()