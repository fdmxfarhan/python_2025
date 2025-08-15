import tkinter as tk
import math
from tkinter import messagebox

window = tk.Tk()
window.geometry('600x400')

def calculate_bmi():
    if vazn.get() < 30:
        messagebox.showerror('مشکل وزن', 'وزن شما خیلی کم است!')
    elif vazn.get() > 200:
        messagebox.showerror('مشکل وزن', 'وزن شما خیلی زیاد است!')
    elif ghad.get() < 50:
        messagebox.showerror('مشکل قد', 'قد شما خیلی کم است!')
    elif ghad.get() > 250:
        messagebox.showerror('مشکل قد', 'قد شما خیلی زیاد است!')
    else:
        l1.config(text='BMI شما: ' + str(math.floor(vazn.get() / ((ghad.get() / 100) ** 2))))

title1 = tk.Label(window, text='نام:', padx=10, pady=10)
title2 = tk.Label(window, text='قد:', padx=10, pady=10)
title3 = tk.Label(window, text='وزن:', padx=10, pady=10)
entry1 = tk.Entry(window, width=20)
ghad = tk.Scale(window, from_=0, to=200, orient='horizontal', length=200)
vazn = tk.Scale(window, from_=0, to=200, orient='horizontal', length=200)
bt1 = tk.Button(window, text='محاسبه BMI', padx=10, pady=10, command=calculate_bmi)
l1 = tk.Label(window, text='BMI شما: ', padx=10, pady=10)
title1.grid(row=0, column=0, padx=10, pady=10)
title2.grid(row=1, column=0, padx=10, pady=10)
title3.grid(row=2, column=0, padx=10, pady=10)
entry1.grid(row=0, column=1, padx=10, pady=10)
ghad.grid(row=1, column=1, padx=10, pady=10)
vazn.grid(row=2, column=1, padx=10, pady=10)
bt1.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
l1.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

window.mainloop()