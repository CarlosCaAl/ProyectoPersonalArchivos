import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import messagebox as mb
from Client import *
import threading
import time

print("\nBienvenido al control remoto del robot\nConéctate escribiendo abajo la IP o reconectándote a la IP más reciente\n")

class Window:
    def __init__(self):
        self.win0 = tk.Tk()
        self.win0.geometry('420x480')
        self.win0.title("RobotAPP")
        self.win0.config(bg='#111125')
        self.win0.protocol('WM_DELETE_WINDOW',self.Destroy)

        self.m = self.Selection(self.mSend,'#66AAFF','#2266BB')
        self.m.NewBTN(self.win0,['Parar','Avanzar','Retroceder','Izquierda','Derecha'],[120,120,120,20,220],[70,20,120,70,70],80,40)

        self.a = self.Selection(self.tSend,'#FFAA66','#BB6622')
        self.a.NewBTN(self.win0,['Modo 1','Modo 2','Modo 3','Modo 4','Modo 5'],[320,320,320,320,320],[20,70,120,170,220],80,40)

        self.AddImage(self.win0,"C:\\Users\\carlo\\OneDrive\\Documentos\\Python\\APP\\Fotos\\Logo.png",20,240,280,160)
        tk.Label(self.win0,text='CARLOS CALDERÓN ALBA').place(x=40,y=260)
        
        self.C = '#FFFFFF'
        self.cBTNd = [0,0]

        self.openWin = [0,0,0]

        tk.Button(self.win0,text='LED',bg='#66FFAA',fg='#111125',command=self.LedWin).place(x=20,y=180,width=80,heigh=40)
        tk.Button(self.win0,text='Servo',bg='#66FFAA',fg='#111125',command=self.ServoWin).place(x=120,y=180,width=80,heigh=40)
        tk.Button(self.win0,text='Matriz',bg='#66FFAA',fg='#111125',command=self.MatrixWin).place(x=220,y=180,width=80,heigh=40)
        tk.Button(self.win0,text='Salir',bg='#FF6666',fg='#111125',command=self.Destroy).place(x=20,y=420,width=80,heigh=40)
        tk.Button(self.win0,text='Vídeo',bg='#AA66FF',fg='#111125',command=self.toogleVideo).place(x=320,y=280,width=80,heigh=40)
        
        self.ipFile = open('C:\\Users\\carlo\\OneDrive\\Documentos\\Python\\APP\\IP.txt','r+')
        self.ip = tk.StringVar()
        self.clientIsOpen = 0
        ipENT = tk.Entry(self.win0,textvariable=self.ip)
        ipENT.place(x=120,y=420,width=120,height=40)
        ipENT.bind('<Key-Return>', self.Connect2)
        tk.Button(self.win0,text='Connect'  ,bg='#66FF66',fg='#111125',command=self.Connect).place(x=240,y=420,width=80,heigh=40)
        tk.Button(self.win0,text='Reconnect',bg='#6666FF',fg='#111125',command=self.Reconnect).place(x=320,y=420,width=80,heigh=40)
        tk.Button(self.win0,text='Detener',bg='#FF6666',fg='#111125',command=self.End).place(x=320,y=380,width=80,heigh=40)

        self.win0.mainloop()

    def toogleVideo(self): 
        if self.clientIsOpen == 1: self.client.toogleVideo()
        else: print("Debes conectarte al servidor antes de enviar cualquier orden\n")

    def Destroy(self):
        try:
            if self.clientIsOpen == 1: self.client.send('close')
        except: print('Se ha perdido la conexion con el servidor, cerrando forzosamente la ventana...')
        self.win0.destroy()

    def Connect2(self,n): self.Connect()
    def Connect(self):
        print("Conectándote al servidor...")
        if self.clientIsOpen == 0: 
            self.client = Client(self.ip.get())
            self.ipFile.write(self.ip.get())
        else: print("Ya estás conectado al servidor !!!\n")
        self.clientIsOpen = 1
        print("Conexión exitosa con el servidor ({}) ;)\n".format(self.ip.get()))
    def Reconnect(self):
        print("Reconectándote al servidor...")
        ip = self.ipFile.read()
        if self.clientIsOpen == 0: self.client = Client(ip)
        else: print("Ya estás conectado al servidor !!!\n")
        self.clientIsOpen = 1
        print("Conexión exitosa con el servidor ({}) ;)\n".format(ip))
    def End(self):
        r = mb.askquestion('Detener el código','Si se detiene el código no se puede volver a iniciar remótamente y se necesitaría encender el ordenador para iniciarlo. Quieres proceder a detenerlo?')
        if r == 'yes':
            if self.clientIsOpen == 1: self.client.send('end')
            else: print("No estás conectado a ningún servidor, se cierra la ventana sin enviar orden\n")
            self.clientIsOpen = 0
            self.Destroy()

    def mSend(self,d):
        if self.clientIsOpen == 1: self.client.send('m'+str(d))
        else: print("Debes conectarte al servidor antes de enviar cualquier orden\n")
    def tSend(self,d): 
        if self.clientIsOpen == 1: self.client.send('t'+str(d))
        else: print("Debes conectarte al servidor antes de enviar cualquier orden\n")

    def ServoWin(self):
        if self.clientIsOpen == 1:
            print("Ventana de los servomotores abierta\n")
            if self.openWin[0] == 0: self.win1 = tk.Toplevel()
            self.openWin[0] = 1
            self.win1.geometry('590x230')
            self.win1.title("Servo")
            self.win1.config(bg='#111125')
            self.win1.protocol('WM_DELETE_WINDOW',self.Destroy1)
            self.Scales = [self.ServoScale(self.win1,'#AA66FF',20 ,20 ,0,self.client),self.ServoScale(self.win1,'#AA66FF',20 ,70 ,1,self.client),self.ServoScale(self.win1,'#66FFAA',210,20 ,2,self.client),self.ServoScale(self.win1,'#66FFAA',210,70 ,3,self.client),self.ServoScale(self.win1,'#66FFAA',210,120,4,self.client),self.ServoScale(self.win1,'#66FFAA',210,170,5,self.client),self.ServoScale(self.win1,'#66AAFF',400,20 ,6,self.client),self.ServoScale(self.win1,'#66AAFF',400,70 ,7,self.client),self.ServoScale(self.win1,'#66AAFF',400,120,8,self.client),self.ServoScale(self.win1,'#66AAFF',400,170,9,self.client)]
            tk.Button(self.win1,text='Guardar' ,bg='#66FF66',fg='#111125',command=self.SaveS).place(x=110,y=170,width=80,heigh=40)
            tk.Button(self.win1,text='Salir',bg='#FF6666',fg='#111125',command=self.Destroy1).place(x=20 ,y=170,width=80,heigh=40)
        else: print("Debes conectarte al servidor antes de enviar cualquier orden\n")
    def Destroy1(self): 
        self.win1.destroy()
        self.openWin[0] = 0
    def SaveS(self):
        for Scale in self.Scales:
            self.client.send('s{}{}   '.format(Scale.index,Scale.val.get()))
            time.sleep(0.05)
    class ServoScale:
        def __init__(self,win,bg,x,y,index,client):
            self.val = tk.IntVar()
            self.index = index
            self.client = client
            tk.Label(win,text='Servo {}'.format(index),bg=bg,fg='#111125').place(x=x,y=y ,width=80,heigh=40)
            tk.Scale(win,fg='#111125',bg=bg,from_=0,to=180,variable=self.val,command=self.func,orient=tk.HORIZONTAL).place(x=x+90,y=y ,width=80,heigh=40)
        def func(self,n): pass
            
    def MatrixWin(self):
        print("Ventana de la matriz LED abierta\n")
        if self.openWin[1] == 0: self.win2 = tk.Toplevel()
        self.openWin[1] = 1
        self.win2.geometry('314x274')
        self.win2.title("Matriz")
        self.win2.config(bg='#111125')
        self.win2.protocol('WM_DELETE_WINDOW',self.Destroy2)
        self.cBTNd[1] = 1
        self.btnC2 = tk.Button(self.win2,text='Color',bg=self.C,fg='#111125',command=self.cSet)
        self.btnC2.place(x=214,y=20,width=80,heigh=40)
        self.p = []
        for j in range(8):
            for i in range(8): self.p.append(self.Pixel(self.win2,20+i*22,20+j*22,self.selectedColor))
        tk.Button(self.win2,text='Borrador',bg='#111125',fg='#FFFFFF',command=self.Eraser  ).place(x=214 ,y=80,width=80,heigh=40)
        tk.Button(self.win2,text='Rellenar',bg='#FFFFFF',fg='#111125',command=self.Fill    ).place(x=214 ,y=140,width=80,heigh=40)
        tk.Button(self.win2,text='Guardar' ,bg='#66FF66',fg='#111125',command=self.SaveM   ).place(x=20 ,y=214,width=77,heigh=40)
        tk.Button(self.win2,text='Salir'   ,bg='#FF6666',fg='#111125',command=self.Destroy2).place(x=117,y=214,width=77,heigh=40)
    def SaveM(self):
        self.Destroy2()
        val = []
        sendVal = 'p'
        if self.clientIsOpen == 1:
            for i in range(8):
                valr = []
                for j in range(8):
                    valr.append(self.p[8*i+j].State())
                    sendVal += self.p[8*i+j].State()
                val.append(valr)
            self.client.send(sendVal)
        else: print("Debes conectarte al servidor antes de enviar cualquier orden\n")
    def Eraser(self):
        self.C = '#000000'
        if self.cBTNd[0] == 1: self.btnC1.config(bg=self.C)
        if self.cBTNd[1] == 1: self.btnC2.config(bg=self.C)
    def Fill(self):
        for i in range(64): self.p[i].Toogle()
    def Destroy2(self):
        self.win2.destroy()
        self.cBTNd[1] = 0
        self.openWin[1] = 0
    class Pixel:
        def __init__(self,win,x,y,colorFunc):
            self.c = '#000000'
            self.func = colorFunc
            self.p = tk.Button(win,text='',bg=self.c,command=self.Toogle)
            self.p.place(x=x,y=y,width=20,heigh=20)
        def Toogle(self):
            self.c = self.func()
            self.p.config(bg=self.c)
        def State(self): return self.c

    def LedWin(self):
        print("Ventana del color abierta\n")
        if self.openWin[2] == 0: self.win3 = tk.Toplevel()
        self.openWin[2] = 1
        self.win3.geometry('220x250')
        self.win3.title("LED")
        self.win3.config(bg='#111125')
        self.win3.protocol('WM_DELETE_WINDOW',self.Destroy3)
        self.cBTNd[0] = 1
        self.btnC1 = tk.Button(self.win3,text='Color',bg=self.C,fg='#111125',command=self.cSet)
        self.btnC1.place(x=20,y=20,width=180,heigh=40)
        self.c = self.Selection(self.cMode,'#FF66AA','#BB2266')
        self.c.NewBTN(self.win3,['Luz 1','Luz 2','Luz 3','Luz 4'],[20,20,120,120],[80,130,80,130],80,40)
        tk.Button(self.win3,text='Salir',bg='#FF6666',fg='#111125',command=self.Destroy3).place(x=20,y=190,width=80,heigh=40)
    def cSet(self):
        c = askcolor(color=self.C,title='COLOR')
        if self.clientIsOpen == 1: self.client.send('lc'+c[1])
        else: print("Debes conectarte al servidor antes de enviar cualquier orden\n")
        self.C = c[1]
        if self.cBTNd[0] == 1: self.btnC1.config(bg=c[1])
        if self.cBTNd[1] == 1: self.btnC2.config(bg=c[1])
    def cMode(self,m):
        if self.clientIsOpen == 1: self.client.send('lm'+str(m))
        else: print("Debes conectarte al servidor antes de enviar cualquier orden\n")
    def selectedColor(self): return self.C
    def Destroy3(self):
        self.win3.destroy()
        self.cBTNd[0] = 0
        self.openWin[2] = 0

    class Selection:
        def __init__(self,func,color,color2):
            self.state = 0
            self.BTN = []
            self.read = []
            self.func = func
            self.color = color
            self.color2 = color2
            self.BTNf = [self.BTN0,self.BTN1,self.BTN2,self.BTN3,self.BTN4]
        def NewBTN(self,win,txt,x,y,w,h):
            for i in range(len(txt)):
                self.read.append(tk.IntVar())
                self.read[i].set(0)
                self.BTN.append(tk.Button(win,text=txt[i],bg=self.color,fg='#111125',command=self.BTNf[i]))
                self.BTN[i].place(x=x[i],y=y[i],width=w,heigh=h)
        def BTN0(self): self.Show(0)
        def BTN1(self): self.Show(1)
        def BTN2(self): self.Show(2)
        def BTN3(self): self.Show(3)
        def BTN4(self): self.Show(4)
        def Show(self,state):
            self.state = state
            for i in range(1,len(self.BTN)):
                if i == self.state: self.BTN[i].config(bg=self.color2)
                else: self.BTN[i].config(bg=self.color)
            n = self.func(self.state) 

    def AddImage(self,win,path,x,y,w,h):
        img = tk.PhotoImage(file=path)
        lbl = tk.Label(win)
        lbl.place(x=x,y=y,width=w,height=h)
        lbl.configure(image=img)
        lbl.image = img

win=Window()