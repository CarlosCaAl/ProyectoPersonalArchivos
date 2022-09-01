import RPi.GPIO as Pin
import time as t

Pin.setwarnings(False)
Pin.setmode(Pin.BCM)

class Ultrasonic:

    def __init__(self,tpin=23,epin=24):
        self.trigPin = tpin
        self.echoPin = epin
        Pin.setup(self.trigPin,Pin.OUT)
        Pin.setup(self.echoPin,Pin.IN)
        Pin.output(self.trigPin,False)
    
    def read(self,d=2):
        Pin.output(self.trigPin,True)
        t.sleep(0.00001)
        Pin.output(self.trigPin,False)

        self.time1 = 0
        self.time2 = 0
        self.time3 = 0
        self.c = 0

        while Pin.input(self.echoPin) == 0: self.c+=1
        self.time1 = t.time()
        while Pin.input(self.echoPin) == 1: self.c+=1
        self.time2 = t.time()

        self.time3 = self.time2-self.time1
        self.distancia = self.time3/0.000058
        self.distancia = round(self.distancia,d)
        return self.distancia