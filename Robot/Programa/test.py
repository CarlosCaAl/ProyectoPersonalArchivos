from Componentes import *
import sys

motor = Motor()
ultrasonic = Ultrasonic()
servo = Servo()

if sys.argv[1] == 'Motor':
    motor.front(100)
    motor.back(100)
    motor.left(90)
    motor.right(90)
    motor.stop()

if sys.argv[1] == 'Ultrasonic':
    while True:
        print(ultrasonic.read())
        t.sleep(1)

if sys.argv[1] == 'Servo':
    while True:
        servo.girar(int(input('ANGLE: ')))