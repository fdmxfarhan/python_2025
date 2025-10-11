import tkinter as tk

window = tk.Tk()
window.geometry('500x600')
minute = 0
second = 0
hour = 0
milisecod = 0
counting = False

def sayHi():
    global counting, second, minute, hour, milisecod
    l1.config(text=str(hour) + ':' + str(minute) + ':' + str(second) + ':' + str(milisecod))
    if counting: 
        milisecod = milisecod + 1
        if milisecod == 100:
            milisecod = 0
            second = second + 1
        if second == 60:
            second = 0
            minute = minute + 1
        if minute == 60:
            minute = 0
            hour = hour + 1
    window.after(10, sayHi)

def stop_click():
    global counting
    counting = False
def start_click():
    global counting
    counting = True
def reset_click():
    global counting, second, minute, hour, milisecod
    counting = False
    second = 0
    minute = 0
    hour = 0
    milisecod = 0


l1 = tk.Label(window, text=str(hour) + ':' + str(minute) + ':' + str(second), font=('Tahoma', 40))
stop_btn = tk.Button(window, text='STOP', font=('tahoma', 20), padx=10, pady=10, command=stop_click)
start_btn = tk.Button(window, text='START', font=('tahoma', 20), padx=10, pady=10, command=start_click)
reset_btn = tk.Button(window, text='RESET', font=('tahoma', 20), padx=10, pady=10, command=reset_click)
l1.pack()
stop_btn.pack()
start_btn.pack()
reset_btn.pack()
sayHi()

window.mainloop()