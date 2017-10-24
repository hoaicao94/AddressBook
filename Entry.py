import Tkinter as tk
from Tkinter import Image

FILENAME = 'image.png'
root = tk.Tk()
canvas = tk.Canvas(root, width=250, height=250)
canvas.pack()
tk_img = Image.PhotoImage(file = FILENAME)
canvas.create_image(125, 125, image=tk_img)
quit_button = tk.Button(root, text = "Quit", command = root.quit, anchor = 'w',
                    width = 10, activebackground = "#33B5E5")
quit_button_window = canvas.create_window(10, 10, anchor='nw', window=quit_button)
root.mainloop()