import RPi.GPIO as GPIO
import time

BUZZER=12
SW1=5
SW2=6
SW3=13
SW4=19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

p=GPIO.PWM(BUZZER, 261)
p.start(0)
m=[392, 330, 349, 294] # 순서대로 솔, 미, 파, 레

try:
    while True: # 솔 미 미 파 레 레=sw1 sw2 sw2 sw3 sw4 sw4=나비야 나비야
        sw1Value=GPIO.input(SW1)
        sw2Value=GPIO.input(SW2)
        sw3Value=GPIO.input(SW3)
        sw4Value=GPIO.input(SW4)
        
        if(sw1Value==1): # 스위치1 누르면 솔
            p.start(5)
            p.ChangeFrequency(m[0])
            time.sleep(0.1)
            p.stop()
        if(sw2Value==1): # 스위치2 누르면 미
            p.start(5)
            p.ChangeFrequency(m[1])
            time.sleep(0.1)
            p.stop()
        if(sw3Value==1): # 스위치3 누르면 파
            p.start(5)
            p.ChangeFrequency(m[2])
            time.sleep(0.1)
            p.stop()
        if(sw4Value==1): # 스위치4 누르면 레
            p.start(5)
            p.ChangeFrequency(m[3])
            time.sleep(0.1)
            p.stop()
        
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()