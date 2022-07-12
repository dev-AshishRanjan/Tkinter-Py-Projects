import matplotlib
import cmasher as cmr
from tkinter import *
from threading import Timer
import numpy as np

root=Tk()
root.title('Color Palette')

#Creating The Welcome 
l1=Label(root,text='Welcome\n\n', fg='purple',font=8,padx=100,pady=80)
l1.grid(row=0,column=0,columnspan=3)
l2=Label(root,text='COLOR  PALETTE\n\n', fg='purple',font=14,padx=100,pady=80)
l2.grid(row=1,column=0,columnspan=3)
def clear1():
    global l1
    global l2
    l1.grid_forget()
    l2.grid_forget()
    window1()

timer=Timer(2,clear1)
timer.start()

def color_name(value):
    global color_button
    global colors
    
    l=Label(root,text=colors[value])
    l.grid(row=16,column=0)


def fun():
    global l1
    global e1
    global l2
    global e2
    global l3
    global e3
    global b1
    global color_button
    global colors
    l1.grid_forget()
    e1.grid_forget()
    l2.grid_forget()
    e2.grid_forget()
    l3.grid_forget()
    e3.grid_forget()
    b1.grid_forget()

    colors=cmr.take_cmap_colors(str(e1.get()), int(e2.get()), return_fmt=str(e3.get()) )
    c=np.arange(0,100,1)

    for i in range(int(e2.get())) :
        
        color_button=Button(root,bg=colors[i],bd=2,padx=5,pady=5,command=lambda:color_name(i))
        color_button.grid(row= i%12 , column=c[i//12])

        
            
        


def window1():
    global l1
    global e1
    global l2
    global e2
    global l3
    global e3
    global b1
    l1=Label(root,text='C_Map :',font=8,padx=10,pady=10)
    l1.grid(row=0,column=0,columnspan=2)
    e1=Entry(root)
    e1.grid(row=0,column=2,columnspan=2)

    l2=Label(root,text='Distribution no. :',font=8,padx=10,pady=10)
    l2.grid(row=1,column=0,columnspan=2)
    e2=Entry(root)
    e2.grid(row=1,column=2,columnspan=2)

    l3=Label(root,text='Format :',font=8,padx=10,pady=10)
    l3.grid(row=2,column=0,columnspan=2)
    e3=Entry(root)
    e3.grid(row=2,column=2,columnspan=2)

    b1=Button(root,text='Submit',bd=5,command=fun)
    b1.grid(row=3,column=1,columnspan=2)





root.mainloop()