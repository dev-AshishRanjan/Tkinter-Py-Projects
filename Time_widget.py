

from tkinter import *
import datetime
import time
from threading import Timer

root=Tk()
root.title('Time')

#t=time.time()
l1=Label(root,text=str(datetime.datetime.now()), bd=5)
l1.grid(row=0,column=0)


def time_update():
    global l1
    #l1.grid_forget()

    l1.config(text=str(datetime.datetime.now()))
    time_update()


time_update()


root.mainloop()
