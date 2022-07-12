from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import cmasher as cmr
from mpl_toolkits import mplot3d

root=Tk()
#root.geometry("300x300")
root.configure(bg="cyan")
r=2

#defining line graph
def line():
    x=np.linspace(0,20,300)
    y_test=np.sin(x) 
    noise=np.random.rand(300)
    y=np.add(y_test,noise)
    plt.plot(x,y,"red",linestyle="-.", marker="p", alpha=0.5,)
    plt.show()

#defining histogram 
def hist():
    x=np.random.normal(2000, 250, 500)
    y=np.random.normal(2000, 250, 500)
    plt.hist(x, 500)
    plt.show()

#creating scatter plot
def scatter():
    x=np.random.normal(2000, 250, 500)
    y=np.random.normal(2000, 250, 500)
    plt.scatter(x,y,s=x/50, c=y,alpha=0.5)
    plt.show()

#defining pie chart
def pie():
    x=np.random.randint(0,30,10)
    y=[str(i) for i in range(10)]
    explode=[0,1,0,0,1,0,1,0,0,1]
    colors=cmr.take_cmap_colors("hsv", 10, return_fmt="hex")
    plt.pie(x,labels=colors,explode=explode, colors=colors,shadow=True)
    plt.legend()
    plt.show()

#defining the bar on axis plot

# Fixing random state for reproducibility
def special1():
    
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # Compute pie slices
    N = 20
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4 * np.random.rand(N)
    colors = plt.cm.twilight(radii / 10.)

    ax = plt.subplot(projection='polar')
    ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)

    plt.show()

#defining polar plot
#this method was used by john elder from codemy.com
def polar():
    x=np.random.normal(2000, 250, 10)
    y=np.random.normal(2000, 250, 10)
    plt.polar(x)
    plt.show()

#defining scatter on polar axis
def special2():
    x=np.random.normal(2000, 250, 500)
    y=np.random.normal(2000, 550, 500)
    fig=plt.figure()
    ax=fig.add_subplot(projection="polar")
    ax.scatter(x,y,s=x/50, c=y,cmap="twilight",alpha=0.8)     # method from matplotlib documentation
    plt.show()

#defining 3d
def threeD():
    x=np.random.normal(2000, 250, 50)
    y=np.random.normal(2000, 550, 50)
    X,Y=np.meshgrid(x,y)

    Z=np.sin(X)+np.cos(Y)
    fig=plt.figure()
    ax=plt.axes(projection="3d")
    ax.plot_surface(X,Y,Z,cmap="viridis",alpha=0.8)    
    plt.show()



def plot():
    global r

    if r.get()==1:
        line()
    elif r.get()==2:
        hist()
    elif r.get()==3:
        scatter()
    elif r.get()==4:
        pie()
    elif r.get()==5:
        special1()
    elif r.get()==6:
        polar()
    elif r.get()==7:
        special2()
    elif r.get()==8:
        threeD()

    

#creating radio buttons
r=IntVar()
r.set("4")
Radiobutton(root,text="line graph",variable=r, value=1,bg="cyan",font=8).grid(row=0,column=0,columnspan=2,sticky=W)
Radiobutton(root,text="histogram ",variable=r, value=2,bg="cyan",font=8).grid(row=1,column=0,columnspan=2,sticky=W)
Radiobutton(root,text="scatter graph",variable=r, value=3,bg="cyan",font=8).grid(row=2,column=0,columnspan=2,sticky=W)
Radiobutton(root,text="pie plot",variable=r, value=4,bg="cyan",font=8).grid(row=3,column=0,columnspan=2,sticky=W)
Radiobutton(root,text="bar on polar axis",variable=r, value=5,bg="cyan",font=8).grid(row=4,column=0,columnspan=2,sticky=W)
Radiobutton(root,text="polar graph",variable=r, value=6,bg="cyan",font=8).grid(row=5,column=0,columnspan=2,sticky=W)
Radiobutton(root,text="scatter on polar axis",variable=r, value=7,bg="cyan",font=8).grid(row=6,column=0,columnspan=2,sticky=W)
Radiobutton(root,text="3D plot",variable=r, value=8,bg="cyan",font=8).grid(row=7,column=0,columnspan=2,sticky=W)

but=Button(root, text="plot", command=plot,padx=5,pady=5,bd=5,bg="white",font=8)
but.grid(row=8,column=1,columnspan=1,sticky=W,pady=10)

root.mainloop()