# برنامه تاس 6 تایی
import tkinter as tk
import random

window = tk.Tk()

def roll_dice():
    r = random.randint(1, 6)
    l1.config(text=r)

b1 = tk.Button(window, text='انداختن تاس', command=roll_dice)
l1 = tk.Label(window, text='-')
b1.pack()
l1.pack()

window.mainloop()