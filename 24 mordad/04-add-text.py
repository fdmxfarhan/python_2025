import tkinter as tk
import math
from tkinter import messagebox

window = tk.Tk()
window.geometry('600x400')

text = ''

def add_text(a):
    global text
    text = text + a
    l1.config(text=text)
def mosavi():
    global text
    print(eval(text))


l1 = tk.Label(window, text=text, padx=10, pady=10)
btn1 = tk.Button(window, text='1', padx=10, pady=10, command=lambda: add_text('1'))
btn2 = tk.Button(window, text='0', padx=10, pady=10, command=lambda: add_text('0'))
btn4 = tk.Button(window, text='+', padx=10, pady=10, command=lambda: add_text('+'))
btn3 = tk.Button(window, text='=', padx=10, pady=10, command=mosavi)
l1.pack()
btn1.pack()
btn2.pack()
btn4.pack()
btn3.pack()

window.mainloop()