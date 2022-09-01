import socket
import threading
import pickle
import struct
import time as t
import cv2 as cv

class Server:
    def __init__(self,func,host='192.168.43.186'):
        self.func = func
        port1,port2 = 8000,8888  
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server.bind((host,port1))
            port = port1
        except:
            try:
                self.server.bind((host,port2))
                port = port2
            except: print("ERROR ABRIENDO EL SERVIDOR: Prueba a cambiar el puerto o la IP y comprueba tu conexión WiFi")
        self.server.listen()
        print("Servidor abierto en el host '{}', en el puerto {} :)".format(host,port))
        print("Escribe en la caja de texto de la APP la IP y presiona 'Conectar'")
        self.connect()
        self.cap = cv.VideoCapture(0)
        self.recvThread = threading.Thread(target = self.recvLoop)
        self.recvThread.start()

    def connect(self):
        self.client = None
        self.adress = None
        self.client,self.adress = self.server.accept()
        print('El cliente se ha conectado desde la direción: {}'.format(str(self.adress)))

    def send(self,msg,cliente): cliente.send(msg.encode('utf-8'))
    def recv(self,cliente): return cliente.recv(1024).decode('utf-8')

    def sendVide(self):
        _,frame = self.cap.read()
        frame = cv.resize(frame,(280,210),interpolation = cv.INTER_CUBIC)
        a = pickle.dumps(frame)
        self.client.sendall(struct.pack("Q",len(a))+a)

    def recvLoop(self):
        while True:
            r = self.recv(self.client)
            if r == 'close': 
                print('El cliente se ha desconectado')
                self.connect()
            elif r == 'end': 
                print('El cliente ha ordenado detener el código')
                break
            elif r == 'video':
                self.sendVide()
            elif r != '': n = self.func(r)