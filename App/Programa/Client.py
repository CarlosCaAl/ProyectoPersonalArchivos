import socket
import threading
import time
import cv2 as cv
import pickle
import struct

#C:\Users\carlo\OneDrive\Documentos\Python\APP\IP.txt

class thread(threading.Thread):
    def __init__(self,func):
        super(thread,self).__init__()
        self.interations = 0
        self.daemon = False
        self.paused = False
        self.state = threading.Condition()
        self.func = func
    def run(self):
        self.resume()
        while True:
            n = self.func()
            with self.state:
                if self.paused == True: self.state.wait()
        self.interations += 1
    def pause(self):
        with self.state: self.paused = True
    def resume(self):
        with self.state:
            self.paused = False
            self.state.notify()

class Client:
    def __init__(self,ip='192.168.43.186'):
        self.host,self.port1,self.port2 = ip,8000,8888
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()
        self.recvVideo()
        self.videoThread = thread(self.recvVideo)
        self.videoThread.start()
        self.video = 0
    def connect(self):
        while True:
            try:
                self.client.connect((self.host,self.port1))
                break
            except:
                time.sleep(0.5)
                try:
                    self.client.connect((self.host,self.port2))
                    break
                except: time.sleep(0.5)

    def recv(self):
        try:
            msg = self.client.recv(1024).decode('utf-8')
            print(msg)
            return msg
        except:
            print('Ocurrió un error\nDesconectándote del servidor\nIntenta conectarte de nuevo dentro de un rato')
            self.client.close()
            return "error"

    def send(self,msg):
        self.client.send(msg.encode('utf-8'))

    def toogleVideo(self):
        if self.videoThread.paused == False: self.videoThread.pause()
        else: self.videoThread.resume()

    def recvVideo(self):
        size = struct.calcsize("Q")
        self.send('video')
        data = b""
        while len(data) < size:
            packet = self.client.recv(4*1024)
            if not packet: break
            data += packet
        msgSize1 = data[:size]
        data = data[size:]
        msgSize2 = struct.unpack("Q",msgSize1)[0]
        while len(data) < msgSize2: data += self.client.recv(4*1024)
        frameData = data[:msgSize2]
        frame = pickle.loads(frameData)
        cv.imshow("Camara",frame)
        time.sleep(0.5)