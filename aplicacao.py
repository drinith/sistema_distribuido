#!/usr/bin/python
# -*- coding: <UTF-8> -*-
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
    from MQTT import MqttPublish 
    
class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        self.ligar = Button(self.container8, text="Ligar", font=self.fonte, width=12)
        self.ligar["command"] = self.ligar
        self.ligar.pack (side=LEFT)
  
        self.desligar = Button(self.container8, text="Desligar", font=self.fonte, width=12)
        self.desligar["command"] = self.desligar
        self.desligar.pack (side=LEFT)
       
  
    def ligar(self):
        publish = MqttPublish()
        publish.publicar("b","1")
        
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O bot�o recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"

    def desligar(self):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O bot�o recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"
  
  
root = Tk()
Application(root)
root.mainloop()
