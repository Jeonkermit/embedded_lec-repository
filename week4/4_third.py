import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD) #use BCM mode or BOARD mode
GPIO.setup(36, GPIO.OUT) # BCM모드로 16번 핀
GPIO.setup(40, GPIO.OUT) # BCM모드로 21번 핀
GPIO.setup(38, GPIO.OUT) # BCM모드로 20번 핀
GPIO.setup(37, GPIO.OUT) # BCM모드로 26번 핀

list=[36, 40, 38, 37]
i=0
while i<10: # i가 10보다 크면 반복문 종료
    randomL=random.choice(list)
    GPIO.output(randomL, GPIO.HIGH) # 핀 on
    time.sleep(0.5)
    GPIO.output(randomL, GPIO.LOW) # 핀 off
    time.sleep(0.5)
    i+=1
    