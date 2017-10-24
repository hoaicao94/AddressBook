#!/usr/bin/env python
import Tkinter as tk

def option1(self):
    print("testing")


top = tk.Tk()
tex = tk.Text(master=top)
tex.pack(side=tk.BOTTOM)
bop = tk.Frame()
bop.pack(side=tk.TOP)


button = tk.Button(bop, text="View All Contacts", command=option1)
button.pack()

button = tk.Button(bop, text="View All Contacts", command=option1)
button.pack()

button = tk.Button(bop, text="View All Contacts", command=option1)
button.pack()

button = tk.Button(bop, text="View All Contacts", command=option1)
button.pack()

tk.Button(bop, text='Exit', command=top.destroy).pack()
top.mainloop()
