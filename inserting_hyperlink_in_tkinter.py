#Import the required libraries
from tkinter import *
import webbrowser

#Create an instance of tkinter frame
root = Tk()
root.geometry("450x250")

#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

#Create a Label to display the link
my_label = Label(root, text="www.google.com",font=('Helveticabold', 15), fg="red", cursor="hand2")     #cursor parameter changes cursor to hand
my_label.pack()
my_label.bind("<Button-1>", lambda e : callback("https://www.google.com/search?q=hero"))        #binding to link

root.mainloop()