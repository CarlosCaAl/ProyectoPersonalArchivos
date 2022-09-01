import smtplib as smtp

class Mail:
    def __init__(self):
        self.addr,self.port = 'smtp.gmail.com',587
        passwordFile  = open('/home/pi/Desktop/PP/Robot/Codigo/files/password.txt','r+')
        self.password,self.mail = passwordFile.read(),'carlos.calderonalba@mascamarena.es'
        self.server = smtp.SMTP(self.addr,self.port)
        self.server.starttls()
        self.server.login(self.mail,self.password)
        self.mailCarlos = 'carlos.calderonalba@gmail.com'
    def send(self,to,subject,body):
        msg = 'Subject: {}\n\n{}'.format(subject,body)
        self.server.sendmail(self.mail,to,msg)

    def quit(self): self.server.quit()

mailSender = Mail()
mailSender.send(to=mailSender.mailCarlos,subject='Correo de python',body='Hola :)')
mailSender.quit()