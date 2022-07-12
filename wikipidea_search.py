#creating multilingual wikipidea search appplication

#Import the required libraries
from tkinter import *
import webbrowser
from PIL import ImageTk, Image

#Create an instance of tkinter frame
root = Tk()
root.geometry("400x500")
root.configure(background="black")
root.title("WIKI")

#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)


my_img=ImageTk.PhotoImage(Image.open("images/wiki1.jpg"))
my_label = Label(root,image=my_img, cursor="hand2", bg="black")     #cursor parameter changes cursor to hand
my_label.grid(row=0,column=0,columnspan=2 ,pady=30,padx=20)
my_label.bind("<Button-1>", lambda e : callback("https://www.wikipedia.org/" ))

label1=Label(root,text="Search Data", bg="black", fg="white").grid(row=1,column=0,padx=20)
entry=Entry(root,bg="white", fg="black", width=20,font="century" )
entry.grid(row=1,column=1, pady=20,padx=20)

#creating entry for language selection
label2=Label(root,text="Language", bg="black", fg="white").grid(row=2,column=0,padx=20)
entry2=Entry(root,bg="white", fg="black", width=20,font="century" )
entry2.grid(row=2,column=1, pady=20,padx=20)
entry2.insert(0,"en")


button=Button(root,text="Search", fg="white",bd=5,bg="black",padx=20,cursor="hand2")
button.grid(row=3,column=0,columnspan=2)

button.bind("<Button-1>", lambda e : callback("https://"+ str(entry2.get()) +".wikipedia.org/wiki/"+ str(entry.get()) ))        #binding to link

#creating a hyperlink for language description
label3=Label(root,text="For Language selection/abbreviation please click It ", bg="black", fg="skyblue", cursor="center_ptr")
label3.grid(row=4,column=0,columnspan=2,pady=10)
label3.bind("<Button-1>", lambda e : callback("https://www.wikipedia.org/" ))

root.mainloop()
 # url:: https://en.wikipedia.org/wiki/