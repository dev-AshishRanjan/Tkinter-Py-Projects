from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry("400x400")
root.title("gif")
img=ImageTk.PhotoImage(Image.open("images/1.jpeg"))
label=Label(root,image=img)
label.pack()


root.mainloop()