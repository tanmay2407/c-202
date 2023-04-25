import socket
from threading import Thread
from tkinter import *
# nickname = input("Enter Name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '127.0.0.1'
port = 8000
client.connect((ip,port))

class GUI:
  def goAhead(self, name):
    self.login.destroy()
    self.name = name
    rcv = Thread(target=self.recieve)
    rcv.start()
  
  def recieve(self):
    while True:
      try:
        message = client.recv(2048).decode("utf-8")
        if message == "NICKNAME":
          client.send(self.name.encode("utf-8"))
        else:
          pass
      except:
        print("An error occured!")
        client.close()
        break

  def __init__(self):
    self.Window = Tk()
    self.Window.withdraw()

    self.login = Toplevel()
    self.login.title("Login")
    self.login.resizable(width=False, height=False)
    self.login.configure(width=500, height=500)

    self.titleLabel = Label(
      self.login, 
      text="Login Screen", 
      bd=4, fg="#2f3436", 
      font="Helvetica 16 bold", 
      justify=CENTER)
    self.titleLabel.place(x=180, y=50)

    self.nameLabel = Label(
      self.login, 
      text="Username:", 
      bd=4, fg="#2f3436", 
      font="Helvetica 12 bold", 
      justify=CENTER)
    self.nameLabel.place(x=100, y=100)
    self.nameEntry = Entry(self.login, font="Helvetica 12 bold")
    self.nameEntry.place(x=220, y=100)

    self.go = Button(
      self.login, 
      text="Login", 
      background="#6e818a", 
      bd=4, fg="#e8e8e8", 
      font="Helvetica 14 bold", 
      justify=CENTER, 
      command=lambda: self.goAhead(self.nameEntry.get()))
    self.go.place(x=210, y=150)

    self.Window.mainloop()

GUI()

# def write():
#   while True:
#     message = "{}:{}".format(nickname,input(""))
#     client.send(message.encode("utf-8"))

# recvThread = Thread(target=recieve)
# recvThread.start()

# writeThread = Thread(target=write)
# writeThread.start()

