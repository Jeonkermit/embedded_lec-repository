import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #use BCM mode or BOARD mode
GPIO.setup(36, GPIO.OUT) # BCM모드로 16번 핀
GPIO.setup(40, GPIO.OUT) # BCM모드로 21번 핀
GPIO.setup(38, GPIO.OUT) # BCM모드로 20번 핀
GPIO.setup(37, GPIO.OUT) # BCM모드로 26번 핀


while True:
    try:
        GPIO.output(36, GPIO.HIGH) # BCM모드로 16번 핀 on(왼위)
        GPIO.output(40, GPIO.HIGH) # BCM모드로 21번 핀 on(오위)
        GPIO.output(38, GPIO.HIGH) # BCM모드로 20번 핀 on(오아래)
        GPIO.output(37, GPIO.HIGH) # BCM모드로 26번 핀 on(왼아래)
    except KeyboardInterrupt:
        GPIO.cleanup() # LED핀 reset
        exit() # 컨트롤+C -> LED 모두 off