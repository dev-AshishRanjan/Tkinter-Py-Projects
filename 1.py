from tkinter import *

root1=Tk()
def fun():
    global root1
    root1.quit()
    global root2
    root2=Tk()
    b=Button(root2, text='Exit lol', command=root2.quit).pack()
    
b=Button(root1, text='Exit', command=fun).pack()



root1.mainloop()
root2.mainloop()
