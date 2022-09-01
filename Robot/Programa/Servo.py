import RPi.GPIO as Pin
import time as t

Pin.setwarnings(False)
Pin.setmode(Pin.BCM)

class Servo:
    def __init__(self,pin,stp=1,angle=90):
        self.pin = pin
        self.stp = stp
        self.mem = angle
        Pin.setup(self.pin, Pin.OUT)
        self.girar(self.mem)

    def pulse(self,v):
        width = (v * 11.11 + 500) / 1000000
        Pin.output(self.pin,1)
        t.sleep(width)
        Pin.output(self.pin,0)
        t.sleep(width)
    
    def girar(self,a):
        if a > self.mem:
            for i in range(self.mem,a,1 ): self.pulse(i)
        if a < self.mem:
            for i in range(self.mem,a,-1): self.pulse(i)
        for i in range(12): self.pulse(a)
        self.mem = a