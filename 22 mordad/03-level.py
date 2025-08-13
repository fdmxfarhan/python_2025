import tkinter as tk

window = tk.Tk()
window.geometry('500x600')

levels = ['مرحله اول: این مرحله اول است', 'مرحله دوم...', 'مرحله سوم', 'مرحله آخر']
current_level = 0

def next_click():
    global current_level, levels
    if current_level < len(levels)-1: current_level = current_level + 1
    l1.config(text=levels[current_level])
def prev_click():
    global current_level, levels
    if current_level > 0: current_level = current_level - 1
    l1.config(text=levels[current_level])



l1 = tk.Label(window, font=('Tahoma', 20), text=levels[current_level])
next_btn = tk.Button(window, font=('Tahoma', 20), text='Next', command=next_click)
prev_btn = tk.Button(window, font=('Tahoma', 20), text='Previous', command=prev_click)
l1.pack()
next_btn.pack()
prev_btn.pack()




window.mainloop()
