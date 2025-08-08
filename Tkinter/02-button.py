import tkinter as tk

window = tk.Tk()
window.geometry('800x600')
window.title('آزمایش دکمه ها')

def on_click():
    l1.config(text='کلیک کردی!!!!!!!!')
    
l1 = tk.Label(window, text='این یک متن آزمایشی است')
b1 = tk.Button(window, text='کلیک کنید', width=20, height=4,command=on_click)

b1.pack()
l1.pack()

window.mainloop()