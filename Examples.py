from Tkinter import *
root=Tk()


b=Button(root,justify = LEFT)
photo=PhotoImage(file="addressbook.gif")
b.config(image=photo,width="100",height="100")
b.pack(side=LEFT)


root.mainloop()