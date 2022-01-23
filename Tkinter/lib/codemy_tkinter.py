# ERP - GERENCIAMENTO DE ESTOQUE

# IMPORTS
import tkinter as tk
from tkinter import DISABLED, ttk
from turtle import bgcolor

# WINDOW CONFIGS
window = tk.Tk()  # janela
window.title('Learning Tkinter')  # nome da janela
window.iconbitmap('Tkinter/resources/linux.ico') # nao aceita .png (image), apenas .ico (icon)
width = 400
height = 250
window.geometry(f'{width}x{height}+{int(width/4)}+{int(height/5)}')

# FRAME CONFIGS
frame = tk.Frame(window, width=width, height=height)
frame.grid(ipadx=width, ipady=height)

# BUTTONS FUNCTIONS
def click_btn_label(master, txt=str, row=None, column=None):
    lbl = ttk.Label(master, text=txt)
    lbl.grid(row=row, column=column)

# BUTTONS
btn1 = ttk.Button(
    frame, 
    text='Press to Quit', 
    command=lambda: window.quit()
    )
btn2 = ttk.Button(
    frame, 
    text='Shows Text', 
    command=lambda:click_btn_label(
        frame, 'Shows some text'
        )
    )
btn3 = ttk.Button(
    frame, 
    text='Disabled Button', 
    state=DISABLED
    )

# GRID PLOT
btn1.grid(row=0, column=0, ipadx=10, ipady=10)
btn2.grid(row=1, column=0)
btn3.grid(row=2, column=0)

# END
window.mainloop()  # precisa disso pra janela continuar sendo atualizada. Caso contrário, ela abre e logo fecha.
