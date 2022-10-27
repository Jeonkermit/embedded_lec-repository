import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #use BCM mode or BOARD mode
GPIO.setup(36, GPIO.OUT) # BCM모드로 16번 핀
GPIO.setup(40, GPIO.OUT) # BCM모드로 21번 핀
GPIO.setup(38, GPIO.OUT) # BCM모드로 20번 핀
GPIO.setup(37, GPIO.OUT) # BCM모드로 26번 핀


while True:
    GPIO.output(36, GPIO.HIGH) # BCM모드로 16번 핀 깜빡(왼위)
    time.sleep(1.0)
    GPIO.output(36, GPIO.LOW)
    time.sleep(1.0)
    
    GPIO.output(40, GPIO.HIGH) # BCM모드로 21번 핀 깜빡(오위)
    time.sleep(1.0)
    GPIO.output(40, GPIO.LOW)
    time.sleep(1.0)
    
    GPIO.output(38, GPIO.HIGH) # BCM모드로 20번 핀 깜빡(오아래)
    time.sleep(1.0)
    GPIO.output(38, GPIO.LOW)
    time.sleep(1.0)
    
    GPIO.output(37, GPIO.HIGH) # BCM모드로 26번 핀 깜빡(왼아래)
    time.sleep(1.0)
    GPIO.output(37, GPIO.LOW)
    time.sleep(1.0)
