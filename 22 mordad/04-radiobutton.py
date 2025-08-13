import tkinter as tk

window = tk.Tk()
window.geometry('500x600')
tavafogh = tk.StringVar(value='gozine 1')

rb1 = tk.Radiobutton(window, text='موافقم', variable=tavafogh, value='gozine 1')
rb2 = tk.Radiobutton(window, text='موافق نیستم', variable=tavafogh, value='gozine 2')
rb1.pack()
rb2.pack()


window.mainloop()