import tkinter as tk
import time
from tkinter import *

def timeupdate():
    cur_time = time.strftime('%H:%M:%S')
    clock_lab.config(text=cur_time)
    clock_lab.after(1000, timeupdate)
    
root  = tk.Tk()
root.title('My first clock')

#need to study how to change icon 
#icon_path = 'cl.ico'
#root.iconbitmap(icon_path)

clock_lab = tk.Label(root,font=('Cursive', 50), bg='pink',fg='white')
clock_lab.pack(anchor='center')

timeupdate()

root.mainloop()