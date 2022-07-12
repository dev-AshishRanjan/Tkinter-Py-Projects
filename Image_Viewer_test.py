#  Language : Python
#  Library : Tkinter, PIL
#  This is a test code for Image Viewer.
#  This code's result forms a image viewer app in which images overlaps.
#  the final result shows no overlapping of images.

#Imports
from tkinter import *
from typing import Sized
from PIL import ImageTk, Image

root=Tk()
root.title('IMAGE  Viewer')
root.iconbitmap('images/icon_final.ico')

i=0

#making things thst will appear before images
l=Label(root,text='WELCOME \n\n To an IMAGE viewer created by: \n\n KUMAR ASHISH RANJAN',height=30,bg='pink', fg='red',padx=120)
l.grid(row=0,column=0,columnspan=3)


#Defining the images
my_img1=ImageTk.PhotoImage(Image.open('images/1.jpeg'))
my_img2=ImageTk.PhotoImage(Image.open('images/2.jpeg'))
my_img3=ImageTk.PhotoImage(Image.open('images/3.jpg'))
my_img4=ImageTk.PhotoImage(Image.open('images/4.jfif'))
my_img5=ImageTk.PhotoImage(Image.open('images/6.jpg'))
my_img6=ImageTk.PhotoImage(Image.open('images/7.jpeg'))

#Creating List of defined images
my_list=[my_img1,my_img2,my_img3,my_img4,my_img5,my_img6]


#Defining the Functions
def next():
    l.grid_forget()
    global i
    i += 1
    p=abs(i%5)
    my_label=Label(image=my_list[p], height=500,bg='cyan')
    my_label.grid(row=0,column=0, columnspan=3)

def previous():
    l.grid_forget()
    global i
    i -= 1
    p=abs(i%5)
    my_label=Label(image=my_list[p],height=500,bg='cyan')
    my_label.grid(row=0,column=0, columnspan=3)

#defining Buttons
button_prev=Button(root,text='<<', command=previous, padx=10, pady=10)
button_exit=Button(root,text='Exit', command=root.quit, padx=20, pady=10)
button_next=Button(root,text='>>', command=next, padx=10, pady=10)

#putting the defined buttons on screen
button_prev.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_next.grid(row=1,column=2)

root.mainloop()