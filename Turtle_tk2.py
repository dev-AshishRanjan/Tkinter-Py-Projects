#  C.Language = PYTHON
#  Module = Tkinter, Turtle , Threading, Random, Cmasher
#  fully working code with exception handling


import turtle
import matplotlib
import cmasher as cmr
from tkinter import *
from PIL import ImageTk,Image
from threading import Timer
import numpy as np
import random
from tkinter import messagebox


root=Tk()
root.title('Turtle')
root.geometry("400x400")

#creating labels
l1=Label(root,text='Name').grid(row=0,column=0)
l2=Label(root,text='Turtle Name').grid(row=1,column=0)
l3=Label(root,text='Loop').grid(row=2,column=0)
#creating Entry box
e1=Entry(root,width=35)
e1.grid(row=0,column=1,columnspan=2,padx=10,pady=10)
e1.insert(0,"John")
e2=Entry(root,width=35)
e2.grid(row=1,column=1,columnspan=2,padx=10,pady=10)
e2.insert(0,"bob")
e3=Entry(root,width=35,fg="purple")
e3.grid(row=2,column=1,columnspan=2,padx=10,pady=10)
e3.insert(0,"200")

#creating frame for c maps
frame1=LabelFrame(root,text='color')
frame1.grid(row=3,column=0,columnspan=2)
#creating labels for frame1
l4=Label(frame1,text='C_Map').grid(row=0,column=0)
l5=Label(frame1,text="C_Map's Distribution").grid(row=1,column=0)
#creating entry box for frame1
e4=Entry(frame1,width=35,fg='green')
e4.grid(row=0,column=1,columnspan=1,padx=10,pady=10)
e4.insert(0,'viridis')
e5=Entry(frame1,width=35,fg='purple')
e5.grid(row=1,column=1,columnspan=1,padx=10,pady=10)
e5.insert(0,'20')

#creating submit button
frame2=LabelFrame(root,text='Confirm')
frame2.grid(row=4,column=1,columnspan=2,padx=10,pady=10)





# creating the main function
# this is the turtle part
def fun():
    global e3
    global e4
    global e5
    global problem_label

    bob=turtle.Turtle()
    bob.speed('fastest')

    try:
        #creating the colors
        colors=cmr.take_cmap_colors(str(e4.get()) ,int(e5.get()) , return_fmt='hex')
        for q in range(10):
            p= int(e5.get())
            for i in range (int(e3.get())):
                if abs(bob.xcor()) >=200 or abs(bob.ycor()) >= 200 :
                    bob.penup()
                    bob.goto(-300+p , -300+p)
                    bob.pendown()
                    pass

                bob.color(str(colors[(i*q)%p]))
                bob.forward(i)
                bob.left(i)
                

            bob.penup()
            bob.left(int(e5.get()))
            bob.forward(random.randrange(100,200)*2)
            bob.right(random.randint(100,200)*2)
            bob.forward(int(e3.get()))
            bob.pendown()

    except Exception as ex :
        turtle.bye()   # we don't want the turtle window to open when there is problem
        #global problem
        problem = ex
        #problem_label=Label(root,text=str(problem), fg="red", anchor=W)
        #problem_label.grid(row=5,column=0, sticky= W+E)
        response=messagebox.askyesno("ERROR Occured", f"{problem}\n\n\n\n An ERROR occured in your input\n * TO re-val press YES \n * press NO to quit ")

        if response ==1:
            pass            #we cannot use return keyword. pass does the required work
        else:
            def error_quit():
                root.quit()
                root2.destroy()

            root2=Toplevel()
            root2.geometry("400x400")
            root2.title('Quitting')
            my_label1=Label(root2,text="THANK  YOU \n\n Quitting in 1sec ", padx=50,pady=60,fg='red').pack()

            timer1=Timer(1,error_quit)
            timer1.start()

            


    

    bob.ht()
    turtle.done()

#quitting the window
def quit_fun():
    global root2
    root.quit()
    root2.destroy()
    turtle.bye()

#create the function for submit button
def fun2():
    global root2
    root2=Toplevel()
    root2.geometry("400x400")
    root2.title('Quitting')
    global e1


    #my_img=ImageTk.PhotoImage(Image.open("images/icon.png"))
    my_label1=Label(root2,text="THANK  YOU ", padx=50,pady=10,fg='red').pack()
    my_label1=Label(root2,text=f" {str(e1.get())} ", padx=50,pady=10,fg='purple').pack()
    my_label1=Label(root2,text=f" for using this app ", padx=50,pady=10).pack()
    my_label1=Label(root2,text=f" This application is created by :", padx=50,pady=10).pack() 
    my_label1=Label(root2,text=f" KUMAR ASHISH RANJAN", padx=50,pady=10,fg='red').pack()
    my_label1=Label(root2,text=f" The  App will QUIT in 2 sec", padx=50,pady=20,fg='green').pack()
    

    timer=Timer(2,quit_fun)
    timer.start()



#creating the button
button=Button(frame2,text='OK', command=fun ,bd=5, padx=30,pady=10)
button.grid(row=0,column=0,padx=10,pady=10)

quit_button=Button(root,text='QUIT',command= fun2,fg='red',bd=5, padx=20, pady=10)
quit_button.grid(row=5,column=1,padx=5,pady=5)



root.mainloop()

