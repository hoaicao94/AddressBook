from Tkinter import Tk, Label, Button, Entry
from Tkinter import *
from tkMessageBox import showinfo


class AddressBookGUI:
    phonebook = {}
    def recordContact(self):
        name = self.nameInput.get()
        number = self.numberInput.get()
        self.phonebook[name] = number
        self.submaster.destroy()
    def addContact(self):
        self.submaster = Tk()
        Label(self.submaster, font=('Helvetica', 10, 'bold'), background='black', foreground='white',
              text="What is the name?").grid(row=0)
        Label(self.submaster, font=('Helvetica', 10, 'bold'), background='black', foreground='white',
              text="What is the phone number? (XXX-XXX-XXXX)").grid(row=1)

        self.nameInput = Entry(self.submaster)
        self.numberInput = Entry(self.submaster)
        self.nameInput.grid(row=0, column=1)
        self.numberInput.grid(row=1, column=1)
        Button(self.submaster, font=('Helvetica', 10, 'bold'), background='black', foreground='white',
               text='Enter', command=self.recordContact).grid(row=3, column=0, sticky=W, pady=4)
        self.submaster.mainloop()
    def editContact(self):
        self.submaster = Tk()
        Label(self.submaster, font=('Helvetica', 10, 'bold'), background='black', foreground='white',
              text="What is the name of your contact you want to edit?").grid(row=0)
        Label(self.submaster, font=('Helvetica', 10, 'bold'), background='black', foreground='white',
              text="What is the new phone #? (XXX-XXX-XXXX) ").grid(row=1)

        self.nameInput = Entry(self.submaster)
        self.numberInput = Entry(self.submaster)
        self.nameInput.grid(row=0, column=1)
        self.numberInput.grid(row=1, column=1)
        Button(self.submaster, font=('Helvetica', 10, 'bold'), background='black', foreground='white',
               text='Enter', command=self.recordContact).grid(row=3, column=0, sticky=W, pady=4)
        self.submaster.mainloop()
    def removeContact(self):
        self.submaster = Tk()
        Label(self.submaster, font=('Helvetica', 10, 'bold'), background='black', foreground='white',
              text="What is the name of your contact you want to remove?").grid(row=0)
        self.nameInput = Entry(self.submaster)
        self.nameInput.grid(row=0, column=1)
        Button(self.submaster, font=('Helvetica', 10, 'bold'), background='black', foreground='white',
               text='Enter', command=self.recordRemoveContact).grid(row=3, column=0, sticky=W, pady=4)
        self.submaster.mainloop()
    def recordRemoveContact(self):
        # allows user to remove one of the contact if the number is gone
        del self.phonebook[self.nameInput.get()]
        # deletes the name and number user input
        self.submaster.destroy()
    def printAll(self):
        # this will print all the input contacts user inputted and sort it alphabetically
        baseString = ''
        for name, num in sorted(self.phonebook.items()):
            baseString = baseString + name + ": " + num + "\n"
        showinfo(message=baseString)
    def __init__(self, master):
        self.master = master
        master.title("Address Book")
        self.label = Label(master, font=('Helvetica', 29, 'bold'), background='black', foreground='yellow',
                           text="CONTACT BOOK")
        self.label.pack(side=TOP)
        self.greet_button = Button(master, font=('Helvetica', 13, 'bold'), background='black', foreground='white',
                                   text="Add new Contact", command=self.addContact)
        self.greet_button.pack()
        self.greet_button = Button(master, font=('Helvetica', 13, 'bold'), background='black', foreground='white',
                                   text="Edit Contacts", command=self.editContact)
        self.greet_button.pack()
        self.greet_button = Button(master, font=('Helvetica', 13, 'bold'), background='black', foreground='white',
                                   text="Delete Contacts", command=self.removeContact)
        self.greet_button.pack()
        self.greet_button = Button(master, font=('Helvetica', 13, 'bold'), background='black', foreground='white',
                                   text="View all Contacts", command=self.printAll)
        self.greet_button.pack()
        self.close_button = Button(master, font=('Helvetica', 13, 'bold'), background='black', foreground='white',
                                   text="Close", command=master.destroy)
        self.close_button.pack()
root = Tk()
my_gui = AddressBookGUI(root)
root.mainloop()