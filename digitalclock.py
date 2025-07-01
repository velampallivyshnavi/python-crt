import tkinter as tk
from time import strftime

root=tk.Tk()
root.title("digital clock")

def time():
    string=strftime("%H:%M:%S%p\n%D")
    label.config(text=string)
    label.after(1000,time)

label=tk.Label(root,font=('DS-Digital',50,'bold'),background='pink',foreground='black')
label.pack(anchor='center')

time()
root.mainloop()
