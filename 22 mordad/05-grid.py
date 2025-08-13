import tkinter as tk

window = tk.Tk()
window.geometry('500x600')

b1 = tk.Button(window, text='button 1', height=3)
b2 = tk.Button(window, text='button 2')
b3 = tk.Button(window, text='button 3', width=15)

b1.grid(row=0, column=0, padx=10, pady=10, sticky='w')
b2.grid(row=0, column=1, padx=10, pady=10, sticky='ws')
b3.grid(row=1, column=1, padx=10, pady=10, sticky='w')

window.mainloop()