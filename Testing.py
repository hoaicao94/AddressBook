from Tkinter import Tk, Label, Button
from Tkinter import *

class AddressBookGUI:

    def greet(self):
        print("Testing")

    def __init__(self, master):
        self.master = master
        master.title("Address Book")


        self.label = Label(master, text="This is your address book!")
        self.label.pack()

        self.greet_button = Button(master, text="1. Add new Contact", command=self.greet)
        self.greet_button.pack()

        self.greet_button = Button(master, text="2. Edit Contacts", command=self.greet)
        self.greet_button.pack()

        self.greet_button = Button(master, text="3. Delete Contacts", command=self.greet)
        self.greet_button.pack()

        self.greet_button = Button(master, text="4. View all Contacts", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def AddNew(self):

root = Tk()
my_gui = AddressBookGUI(root)

#b = Button(root,justify = LEFT)
#photo = PhotoImage(file="addressbook.gif")
#b.config(image=photo,width="100",height="100")
#b.pack(side=TOP)

root.mainloop()