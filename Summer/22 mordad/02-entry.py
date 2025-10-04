import tkinter as tk

window = tk.Tk()
window.geometry('500x600')

def on_click():
    print('salam ' + e1.get())

e1 = tk.Entry(window, width=10, font=('Tahoma', 25))
b1 = tk.Button(window, padx=10, pady=10, font=('Tahoma', 20), text='click here', command=on_click)
e1.pack()
b1.pack()




window.mainloop()