from Server import *
from Matrix import *
from Motor import *

matrix = Matrix()
motor  =  Motor()

def contestarPeticiones(val):
    valIndicador = val[0]
    val = val[1:]
    if   valIndicador == 'm':
        if val == '0': print("STOP")
        if val == '1': print("FRONT")
        if val == '2': print("BACK")
        if val == '3': print("LEFT")
        if val == '4': print("RIGHT")
    elif valIndicador == 'l':
        valIndicador2 = val[0]
        val = val[1:]
        if   valIndicador2 == 'm':
            print("Orden para el modo del LED: {}".format(val))
        elif valIndicador2 == 'c':
            print("Orden para el color del LED: {}".format(val))
    elif valIndicador == 't':
        print("Orden para cambiar el modo: {}".format(val))
    elif valIndicador == 'p':
        print("Orden para la matriz: {}".format(val))
    elif valIndicador == 's':
        valIndicador2 = val[0]
        val = val[1:5]
        servo = int(valIndicador2)
        angle = int(val)
        print('Servo {}: {}º'.format(servo,angle))

server = Server(func=contestarPeticiones)