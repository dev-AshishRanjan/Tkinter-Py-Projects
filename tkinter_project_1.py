#  courtesy = freeCodeCamp.org  (youtube)
#  Library = Tkinter

from tkinter import *

root= Tk()

for l in range(10): 
    e = Entry(root, width= 50)
    e.pack()
    e.insert(l, f'enter your name{l} :')


def myclick():
    
     hello='hello '+ e.get()   #e.get() takes the data from last input field
     mylabel= Label(root, text=hello)
     mylabel.pack()


mybutton= Button(root, text= f'submit ', command= myclick)
mybutton.pack()

root.mainloop()
