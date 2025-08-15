import tkinter as tk
import webbrowser

window = tk.Tk()
window.geometry('500x600')

def new_file():
    print('new File clicked')

def exit_btn():
    exit()

def open_google():
    webbrowser.open_new('https://google.com')

menubar = tk.Menu(window)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label='فایل جدید', command=new_file)
file_menu.add_command(label='تنظیمات اولیه')
file_menu.add_command(label='پاک کردن صفحه')
file_menu.add_command(label='تماس با پشتیبانی')
file_menu.add_command(label='خروج', command=exit_btn)
menubar.add_cascade(label='تنظیمات', menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label='آموزش کار با نرم افزار', command=open_google)
help_menu.add_command(label='آموزش کار با نرم افزار')
help_menu.add_command(label='آموزش کار با نرم افزار')
menubar.add_cascade(label='راهنما', menu=help_menu)


window.config(menu=menubar)
window.mainloop()
