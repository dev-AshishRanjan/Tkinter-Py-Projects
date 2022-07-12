
#   This code crashes the TERMINAL

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

    l1=Label(root,text=str(datetime.datetime.now()), bd=5)
    l1.grid(row=0,column=0)


while True :
    timer=Timer(1,time_update)
    timer.start()


root.mainloop()
