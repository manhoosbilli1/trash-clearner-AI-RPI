import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
lidM1 = 26
lidM2 = 13
limClose = 27
limOpen = 22
trashTrig = 4
trashEcho = 8
frontTrig = 23
frontEcho = 24
GPIO.setup(lidM1, GPIO.OUT)
GPIO.setup(lidM2, GPIO.OUT)
GPIO.setup(trashTrig, GPIO.OUT)
GPIO.setup(frontTrig, GPIO.OUT)
GPIO.setup(trashEcho, GPIO.IN)
GPIO.setup(frontEcho, GPIO.IN)

GPIO.setup(limClose, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(limOpen, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonState(button):
    state = False
    if GPIO.input(button) == False:
        time.sleep(0.025)  #sleep for 20 milliseconds
        if GPIO.input(button) == False:
            state = True
        else:
            state = False
    return state

def frontSensorHandler():
    GPIO.output(frontTrig, True)
    time.sleep(0.00001)
    GPIO.output(frontTrig, False)
    while GPIO.input(frontEcho) == 0:
        pass
    pulse_start = time.time()
    while GPIO.input(frontEcho) == 1:   #code will only proceed if this condition is true
        pass
    pulse_end = time.time()     
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)   
    return distance

def trashSensorHandler():
    GPIO.output(trashTrig, True)
    time.sleep(0.00001)
    GPIO.output(trashTrig, False)
    while GPIO.input(trashEcho) == 0:
        pass
    pulse_start = time.time()
    while GPIO.input(trashEcho) == 1:   #code will only proceed if this condition is true
        pass
    pulse_end = time.time()     
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)   
    return distance

def openLid():
    #move until the other switch is pressed
    moveMotor =False
    if GPIO.input(limOpen) == 1:    
        #not pressed
        moveMotor = True
        print("opening lid")
        time.sleep(1)    
    while moveMotor == True:
        GPIO.output(lidM1, 0)  
        GPIO.output(lidM2, 1)
        print("waiting to read switch") 
        if GPIO.input(limOpen) == 0:
            #reached open lid switch means it's opened
            GPIO.output(lidM1, 0)  
            GPIO.output(lidM2, 0)
            print("Reached")
            moveForward = False
            break


def closeLid():
    #move until the other switch is pressed
    moveMotor =False
    if GPIO.input(limClose) == 1:    
        #not pressed
        moveMotor = True
        print("closing lid")
        time.sleep(1)    
    while moveMotor == True:
        GPIO.output(lidM1, 1)  
        GPIO.output(lidM2, 0)
        print("waiting to read switch") 
        if GPIO.input(limClose) == 0:
            #reached open lid switch means it's opened
            GPIO.output(lidM1, 0)  
            GPIO.output(lidM2, 0)
            print("Reached")
            moveForward = False
            break


while True:
#    distance = frontSensorHandler()
#    print(distance)
