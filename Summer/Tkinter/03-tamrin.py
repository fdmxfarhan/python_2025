# برنامه ای بنویسید که با هر بار کلیک عدد نمایش داده شده یکی اضافه شود.
import tkinter as tk
window = tk.Tk()

def count():
    n = int(l1['text']) + 1
    l1.config(text=n)
    
b1 = tk.Button(window, text='شمارش', command=count, font=('IRANSans', 20))
l1 = tk.Label(window, text='0', font=('IRANSans', 20))

b1.pack()
l1.pack()

window.mainloop()