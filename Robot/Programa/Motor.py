import RPi.GPIO as Pin
import time as t
import math

Pin.setwarnings(False)
Pin.setmode(Pin.BCM)

class Motor:
    def __init__(self,v=1,w=1):

        self.pin = [[18,23,24],[16,20,21]]
        self.motorSpeed = 100
        self.v = v
        self.w = w

        for i in range(len(self.pin)):
            for j in range(len(self.pin[i])):
                Pin.setup(self.pin[i][j],Pin.OUT)
        self.pwmA = Pin.PWM(self.pin[0][0],500)
        self.pwmB = Pin.PWM(self.pin[1][0],500)
        self.pwmA.start(0)
        self.pwmB.start(0)

    def giro(self, orientation1, orientation2, speed, wait):
        Pin.output(self.pin[0][1], 1-orientation1)
        Pin.output(self.pin[0][2], orientation1)
        Pin.output(self.pin[1][1], 1-orientation2)
        Pin.output(self.pin[1][2], orientation2)
        self.pwmA.ChangeDutyCycle(speed)
        self.pwmB.ChangeDutyCycle(speed)
        t.sleep(wait)
    
    def stop(self,l = 0): self.giro(1,1,0,l)
    def front(self,l = 0): self.giro(1,1,self.motorSpeed,l / (self.v * 100))
    def back(self, l = 0): self.giro(0,0,self.motorSpeed,l / (self.v * 100))
    def right(self, l = 0):  self.giro(1,0,self.motorSpeed,(l * math.pi) / (self.w * 180))
    def left(self, l = 0):  self.giro(0,1,self.motorSpeed,(l * math.pi) / (self.w * 180))