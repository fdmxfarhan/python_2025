import tkinter as tk

window = tk.Tk()
window.geometry('500x600')

def on_click(a):
    print(a)

b1 = tk.Button(window, command=lambda: on_click('1'), text='1')
b2 = tk.Button(window, command=lambda: on_click('2'), text='2')
b3 = tk.Button(window, command=lambda: on_click('3'), text='3')
b1.pack()
b2.pack()
b3.pack()

window.mainloop()