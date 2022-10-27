import threading
import serial
import time
import RPi.GPIO as GPIO

bleSerial=serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.1)

gData=""

PWMA=18
PWMB=23
AIN1=22
AIN2=27
BIN1=25
BIN2=24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

L_Motor=GPIO.PWM(PWMA, 500)
L_Motor.start(0)
R_Motor=GPIO.PWM(PWMB, 500)
R_Motor.start(0)

def go(): # go
    GPIO.output(AIN1, 0)
    GPIO.output(AIN2, 1)
    L_Motor.ChangeDutyCycle(100)
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 1)
    R_Motor.ChangeDutyCycle(100)
    
def back(): # back
    GPIO.output(AIN1, 1)
    GPIO.output(AIN2, 0)
    L_Motor.ChangeDutyCycle(100)
    GPIO.output(BIN1, 1)
    GPIO.output(BIN2, 0)
    R_Motor.ChangeDutyCycle(100)
    
def right(): # right
    GPIO.output(AIN1, 0)
    GPIO.output(AIN2, 1)
    L_Motor.ChangeDutyCycle(100)
    
def left(): # left
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 1)
    R_Motor.ChangeDutyCycle(100)
    
def stop(): # stop
    GPIO.output(AIN1, 0)
    GPIO.output(AIN2, 1)
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 1)
    R_Motor.ChangeDutyCycle(0)   

def serial_thread():
    global gData
    while True:
        data=bleSerial.readline()
        data=data.decode()
        gData=data
        
def main():
    global gData
    try:
        while True:
            if(gData.find("go")>=0):
                gData=""
                print("ok go")
                go()
            if(gData.find("back")>=0):
                gData=""
                print("ok back")
                back()
            if(gData.find("left")>=0):
                gData=""
                print("ok left")
                left()
            if(gData.find("right")>=0):
                gData=""
                print("ok right")
                right()
            if(gData.find("stop")>=0):
                gData=""
                print("ok stop")
                stop()                            
                
    except KeyboardInterrupt:
        pass
    
if __name__=='__main__':
    task1=threading.Thread(target=serial_thread)
    task1.start()
    main()
    bleSerial.close()
    GPIO.cleanup()