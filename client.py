import socket
from threading import Thread
from tkinter import *

nickname=input("Choose your nickname ")

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_adress="127.0.0.1"
port=5000
client.connect((ip_adress,port))

print("Connected to server")

class GUI:
    def __init__(self):
        self.Window=Tk()
        self.Window.withdraw()
        self.login=Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False,height=False)
        self.login.configure(width=800,height=800)
        self.pls=Label(self.login,
                            text="Login to continue",
                            justify=CENTER,
                            font="arial"
                            )
        self.pls.place(relheight=0.315,relx=0.22,rely=0.107)
        self.labelName=Label(self.login,text="Name = ",font="arial 15")
        self.labelName.place(relheight=0.2,relx=0.1,rely=0.2)


        self.entryName=Entry(self.login,font=12)
        self.entryName.place(relheight=0.122,relwidth=0.64,relx=0.35,rely=0.2)
        self.entryName.focus()
        self.go=Button(self.login,
                            text="continue",font="arial 17",command=lambda : self.goahead(self.entryName.get()))
        self.go.place(relx=0.574,rely=0.555)


        self.Window.mainloop()



    def goahead(self,name):
        self.login.destroy()
        self.name=name
        rcv=Thread(target=self.receive)
        rcv.start()

    def receive():
          while True:
            try:
                message=client.recv(2048).decode("utf-8")
                if message=="NICKNAME":
                    client.send(nickname.encode("utf-8"))
                else:
                    print(message)
            
            except:
                    print("ERRROROROR FOUND")
                    client.close()
                    break
                





f=GUI()
        

