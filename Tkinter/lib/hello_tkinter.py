from tkinter import *
from tkinter import ttk

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid(ipadx=250, ipady=250)

# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

root.mainloop()