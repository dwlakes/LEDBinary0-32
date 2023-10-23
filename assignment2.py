import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)


binary = ""

def setUpLEDs():
    GPIO.setup(11, GPIO.OUT)
    #GPIO.output(11, True)
    GPIO.setup(16, GPIO.OUT)
    

def DecimalToBinary(n):
    
    if n >0:
        DecimalToBinary(n//2)
    global binary
    # concatenates bits
    binary = binary + str(n%2)
    #print(binary)
    
def pos4():
    try:
        # [::-1] reverses string
        if binary[::-1][4] == "1":
            GPIO.setup(11, GPIO.OUT)
            GPIO.output(11, True)
    except IndexError:
        pass
    
def pos3():
     try:
         # [::-1] reverses string
        if binary[::-1][3] == "1":
            GPIO.setup(13, GPIO.OUT)
            GPIO.output(13, True)
     except IndexError:
        pass
        
    
    
def pos2():
    try:
        # [::-1] reverses string
        if binary[::-1][2] == "1":
            GPIO.setup(15, GPIO.OUT)
            GPIO.output(15, True)
    except IndexError:
        pass
    
def pos1():
    try:
        # [::-1] reverses string
        if binary[::-1][1] == "1":
            GPIO.setup(10, GPIO.OUT)
            GPIO.output(10, True)
    except IndexError:
        pass
    
def pos0():
    try:
        # [::-1] reverses string
        if binary[::-1][0] == "1":
            GPIO.setup(12, GPIO.OUT)
            GPIO.output(12, True)
    except IndexError:
        pass
    
def turnOffLights():
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, False)
    GPIO.setup(10, GPIO.OUT)
    GPIO.output(10, False)
    GPIO.setup(15, GPIO.OUT)
    GPIO.output(15, False)
    GPIO.setup(13, GPIO.OUT)
    GPIO.output(13, False)
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, False)
    
    
    
if __name__ == "__main__":
    
    for i in range(32):
        binary = ""
        DecimalToBinary(i)
        print(i)
        print(binary)
        pos4()
        pos3() 
        pos2()
        pos1()
        pos0()
        time.sleep(3)
        turnOffLights()
   
        
      
    time.sleep(3)
    GPIO.cleanup()
    
    