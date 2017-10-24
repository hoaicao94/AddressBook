#from Tkinter import *
#import tkMessageBox

#class Application(Frame):
#    def __init__(self, master = None):
#        Frame.__init__(self,master)
#        self.pack()
#        self.createWidgets()

#    def createWidgets(self):
#        self.nameInput = Entry(self)
#        self.nameInput.pack()
#        self.alertButton = Button(self,text='Hello',command=self.hello)
#        self.alertButton.pack()

#    def hello(self):
#        name = self.nameInput.get() or 'world'
#        tkMessageBox.showinfo('Message','Hello, %s'%name)

from Tkinter import Tk, Button
from time import strftime, localtime
from Tkinter.messagebox

def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n',localtime())


root = Tk()
button = Button(root,text='Click it', command=clicked)

button.pack()
root.mainloop()
