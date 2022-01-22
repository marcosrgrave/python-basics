# ERP - GERENCIAMENTO DE ESTOQUE

import tkinter as tk
from tkinter import ttk

window = tk.Tk()  # janela
window.title('Learning Tkinter')  # nome da janela
window.iconbitmap('C:/Users/m1gra/Documents/Code/Python/Tkinter/resources/linux.ico') # nao aceita .png (image), apenas .ico (icon)

frame = ttk.Frame(window)
frame.grid(ipadx=250, ipady=250)

lbl_frame_size = ttk.Label(frame, text=f'{frame.winfo_width()} x {frame.winfo_height()}')
lbl_frame_size.grid()

btn1 = ttk.Button()

def click_btn1():
    pass


window.mainloop()  # precisa disso pra janela continuar sendo atualizada. Caso contrário, ela abre e logo fecha.