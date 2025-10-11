import tkinter as tk
window = tk.Tk()
window.geometry('800x600')
window.title('My App')

l1 = tk.Label(window, 
              font=('IRANSans', 20),
              text='سلام چطوری', 
              fg='white', 
              bg='blue', 
              padx=60, 
              pady=60)
l1.pack()

window.mainloop()