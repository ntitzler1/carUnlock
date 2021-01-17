

import subprocess
import time
import RPi.GPIO as GPIO
import time



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
pwm=GPIO.PWM(3, 50)

pwm.start(0)


def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(3, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(3, False)
    pwm.ChangeDutyCycle(0)


SetAngle(0)
inRange = False

while True:
    result = subprocess.run(["sudo", "hcitool", "cc", "CC:66:0A:AC:7D:BF"],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    output = result.stdout


    if str(output) == "b''":
        print("device in range")
        inRange = True
        print("unlocking car")
        SetAngle(60)
        SetAngle(0)
        
        time.sleep(5)
    else:
        print("device out of range")
        inRange = False
        print("locking car")
        
    



  