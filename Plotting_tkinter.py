from tkinter import *
import numpy as np
import random
from threading import Timer
import matplotlib.pyplot as plt
import cmasher as cmr

#setting the main root
root=Tk()
root.title('Welcome')
root.iconbitmap('images/icon_def.ico')

#defining global variables
global e1
global e2
global e3
global e4
global e5
global e6
global e7
global e8
global e9
global e10
global e11
global e12
global a
global b
global c
global d
global e
global f
global g
global h
global j

#Creating The Welcome 
l1=Label(root,text='Welcome\n\n', fg='purple',font=8,padx=100,pady=80)
l1.grid(row=0,column=0,columnspan=3)
l2=Label(root,text='THE  PLOTTER\n\n', fg='purple',font=14,padx=100,pady=80)
l2.grid(row=1,column=0,columnspan=3)
def clear1():
    global l1
    global l2
    l1.grid_forget()
    l2.grid_forget()
    window1()

timer=Timer(2,clear1)
timer.start()

###creating the graph function.
def line_plot1():
    global e6
    global e7
    global e8
    global e9
    global e11
    global e12
    global g
    global h
    global x
    global y


    p1=int(e6.get())
    p2=int(e7.get())
    p3=int(e11.get())
    p4=int(e12.get())
    plt.xlim([p1, p3])
    plt.ylim([p2, p4])
    #xticks=np.arange(p1 , p3 ,1)
    #plt.xticks(xticks)
    #yticks=np.arange(p2, p4,1)
    #plt.yticks(yticks)
    plt.xlabel(e8.get())
    plt.ylabel(e9.get())
    
    if g.get()==1:
        plt.tick_params(axis='x', colors='red' ) 
    if h.get()==1:
        plt.tick_params(axis='y', colors='red' ) 

    plt.plot(x,y,linestyle= ':' , color='red' , marker='o'  , markersize=10  , mfc='white' , alpha= 0.8 , label= 'plot'  )
    plt.legend()
    plt.show()   



def bar_plot():
    pass

def pie_plot():
    pass
def scatter_plot():
    global e6
    global e7
    global e8
    global e9
    global e11
    global e12
    global g
    global h
    global x
    global y

    

    plt.xlabel(e8.get())
    plt.ylabel(e9.get())

    if g.get()==1:
        plt.tick_params(axis='x', colors='red' ) 
    if h.get()==1:
        plt.tick_params(axis='y', colors='red' )

    plt.scatter(x,y,alpha=0.8)
    plt.show()

def graph_type():
    
    ##making all required variable global
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global e11
    global e12
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global j
    global x
    global y


    '''
    if type(e1.get()) != list:
        x=list(e1.get())
    else:
        x= e1.get()
    if type(e2.get()) != list:
        y=list(e2.get())
    else:
        y=e2.get()  '''

    x=[i for i in e1.get().split()]
    y=[i for i in e2.get().split()]

    
    if len(x)==len(y):
        root.quit()
        ##defining all about graph
        if str(e3.get())== 'yes':
            plt.minorticks_on()
        if str(e3.get())== 'no':
            plt.minorticks_off()

        if a.get()==1:
            plt.tick_params(labeltop=True)
        if b.get()==1:
            plt.tick_params(labelbottom=True)
        if c.get()==1:
            plt.tick_params(labelright=True)
        if d.get()==1:
            plt.tick_params(labelleft=True)

        if e.get()==1:
            plt.tick_params(direction='in', which='major', top=True,bottom=True,right=True,left=True, length= int(e4.get()))
        if f.get()==1:
            plt.tick_params(direction='in', which='minor', top=True,bottom=True,right=True,left=True , length=int(e5.get()))  

        


    if j.get()==1:
        #line_plot1()
        line_plot1()

    if j.get()==2:
        bar_plot()

    if j.get()==3:
        pie_plot()

    if j.get()==4:
        scatter_plot()

    ''' else :
        l10=Label(root,text='Length of X_Value and Y_value should be same',fg="red").grid(row=9,column=0,columnspan=3)  '''
            

    


#creating 1st window
def window1():
    
    ##making all required variable global variable
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global e11
    global e12
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global j

    #Window1 coding starts:
    root.title('PLOTTER')
    x=Label(root,text="X_Value:",padx=5,pady=5).grid(row=0,column=0)
    y=Label(root,text="Y_Value:",padx=5,pady=5).grid(row=1,column=0)
    e1=Entry(root)
    e1.grid(row=0,column=1,columnspan=3)
    #e1.insert(0,'[ in list format ]')
    e2=Entry(root)
    e2.grid(row=1,column=1,columnspan=3)
    #e2.insert(0,'[ in list format ]')
    frame1=LabelFrame(root,text='Tick_Params',padx=10,pady=10)
    frame1.grid(row=2,column=0,columnspan=4,padx=5,pady=5)



    ###creating tick params: frame1
    minortick=Label(frame1,text="minortick_on :",padx=5,pady=5).grid(row=0,column=0,columnspan=2)
    e3=Entry(frame1)
    e3.insert(0,'yes or no')
    e3.grid(row=0,column=3)

    #creating Label's Radio Buttons
    a=IntVar()
    b=IntVar()
    c=IntVar()
    d=IntVar()
    Radiobutton(frame1,text='Label Top', variable=a, value=1).grid(row=1,column=0)
    Radiobutton(frame1,text='Label Bottom', variable=b, value=1).grid(row=1,column=1)
    Radiobutton(frame1,text='Label Right', variable=c, value=1).grid(row=1,column=2)
    Radiobutton(frame1,text='Label Left', variable=d, value=1).grid(row=1,column=3)

    ###creating major ticks: frame2
    frame2=LabelFrame(root,text='Major_Ticks',padx=10,pady=10)
    frame2.grid(row=3,column=0,columnspan=3,padx=5,pady=5)
    e=IntVar()
    e.set("2")
    Radiobutton(frame2,text='IN', variable=e, value=1).grid(row=0,column=0)
    Radiobutton(frame2,text='OUT', variable=e, value=2).grid(row=0,column=1)
    l=Label(frame2,text='Length of Major Tick :').grid(row=1,column=0,columnspan=2)
    e4=Entry(frame2)
    e4.grid(row=1,column=2)

    ###creating minor ticks: frame3
    frame3=LabelFrame(root,text='Minor_Ticks',padx=10,pady=10)
    frame3.grid(row=4,column=0,columnspan=3,padx=5,pady=5)
    f=IntVar()
    f.set("2")
    Radiobutton(frame3,text='IN', variable=f, value=1).grid(row=0,column=0)
    Radiobutton(frame3,text='OUT', variable=f, value=2).grid(row=0,column=1)
    l=Label(frame3,text='Length of Minor Tick :').grid(row=1,column=0,columnspan=2)
    e5=Entry(frame3)
    e5.grid(row=1,column=2)

    ###doing work on axes : frame4
    frame4=LabelFrame(root,text='AXES',padx=10,pady=10)
    frame4.grid(row=5,column=0,columnspan=3,padx=5,pady=5)

    l1=Label(frame4,text='X_Lim, min:').grid(row=0,column=0,columnspan=1)
    l2=Label(frame4,text='Y_Lim, mmin:').grid(row=1,column=0,columnspan=1)
    l3=Label(frame4,text='X  Label :').grid(row=2,column=0,columnspan=1)
    l4=Label(frame4,text='Y  Label :').grid(row=3,column=0,columnspan=1)
    l8=Label(frame4,text='X_Lim, max:').grid(row=0,column=3,columnspan=1)
    l9=Label(frame4,text='Y_Lim, max:').grid(row=1,column=3,columnspan=1)
    e6=Entry(frame4)
    e6.grid(row=0,column=1,columnspan=1)
    e7=Entry(frame4)
    e7.grid(row=1,column=1,columnspan=1)
    e8=Entry(frame4)
    e8.grid(row=2,column=1,columnspan=2)
    e9=Entry(frame4)
    e9.grid(row=3,column=1,columnspan=2)
    e11=Entry(frame4)
    e11.grid(row=0,column=4,columnspan=1)
    e12=Entry(frame4)
    e12.grid(row=1,column=4,columnspan=1)

    l5=Label(frame4,text='X axis major tick color :').grid(row=4,column=0,columnspan=2)
    l6=Label(frame4,text='Y axis minor tick color :').grid(row=6,column=0,columnspan=2)
    g=IntVar()
    g.set("2")
    h=IntVar()
    h.set("2")
    Radiobutton(frame4,text='RED', variable=g, value=1).grid(row=5,column=0)
    Radiobutton(frame4,text='BLACK', variable=g, value=2).grid(row=5,column=1)
    Radiobutton(frame4,text='RED', variable=h, value=1).grid(row=7,column=0)
    Radiobutton(frame4,text='BLACK', variable=h, value=2).grid(row=7,column=1)


    ###creating plot type part : frame5
    frame5=LabelFrame(root,text='Plot Type',padx=10,pady=10)
    frame5.grid(row=6,column=0,columnspan=4,padx=5,pady=5)

    j=IntVar()
    j.set("2")
    Radiobutton(frame5,text='Line Plot', variable=j, value=1).grid(row=0,column=0)
    Radiobutton(frame5,text='Bar Plot', variable=j, value=2).grid(row=0,column=1)
    Radiobutton(frame5,text='Pie Plot', variable=j, value=3).grid(row=0,column=2)
    Radiobutton(frame5,text='Scatter Plot', variable=j, value=4).grid(row=0,column=3)


    ###defining the submit button:frame6
    frame6=LabelFrame(root,text='CONFIRM',padx=10,pady=10)
    frame6.grid(row=8,column=2,columnspan=2,padx=5,pady=5)
    l7=Label(root,text='C_Map :').grid(row=7,column=0,columnspan=1)
    e10=Entry(root)
    e10.grid(row=7, column=1,columnspan=3)
    button_confirm=Button(frame6,text='Submit',command=graph_type,bd=5)
    button_confirm.grid(row=0,column=0,columnspan=2)

    




    



root.mainloop()