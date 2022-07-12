# url : http://www.omdbapi.com/?apikey=[yourkey]&
# api : 9339eb0a
# can be used after imdb_movie_search.py's data


'''
import requests
import json
api_request=requests.get("http://img.omdbapi.com/?apikey=9339eb0a&t=iron man")
api=json.loads(api_request.content)
print(api)    '''


from tkinter import *
import requests
import json
import webbrowser
from PIL import ImageTk, Image

root=Tk()
#root.geometry("300x200")
root.title("Movie App")
root.configure(bg="lightblue")
root.iconbitmap("images/icon_def.ico")

def fun():
    root2=Toplevel()
    global e1
    root2.title("Movie Data")
    root2.iconbitmap("images/icon_final.ico")
    #root2.geometry("400x730")
    

    try:
        api_request=requests.get("http://www.omdbapi.com/?apikey=9339eb0a&i=" + str(e1.get()))
        api=json.loads(api_request.content)
        p=api
        frame1=LabelFrame(root2,text="Data",pady=10)
        frame1.pack(pady=10)
        for k in p:      
            if k != "Ratings" and k!= "Response" and k!= "Plot" and k!= "Poster" :     
                mylabel=Label(frame1,text= f" {k} : {p[k]}" ,font=("Helvetica", 10),anchor=W)
                mylabel.pack(anchor=W) 
       
        q=api["Ratings"]
        frame2=LabelFrame(root2,text="Ratings", pady=10)
        frame2.pack()
        for i in range(len(q)) :                     
            mylabel=Label(frame2,text= f" {q[i]} " ,font=("Helvetica", 10),anchor=W)
            mylabel.pack(anchor=W)  
        
        frame3=LabelFrame(root2,text="Plot", pady=10)
        frame3.pack()
        r=api["Plot"]
        mylabel=Label(frame3,text=str(r) ,font=("Helvetica", 10),anchor=W)
        mylabel.pack(anchor=W)  

        frame4=LabelFrame(root2,text="Poster", pady=10)
        frame4.pack()
        url=api["Poster"]
        mylabel5=Label(frame4,text=str(url) ,font=("Helvetica", 10),anchor=W , fg="blue")
        mylabel5.pack(anchor=W)
        #Define a callback function
        def callback(url):
            webbrowser.open_new_tab(url)
        mylabel5.bind("<Button-1>", lambda e : callback(str(url))) 


        quit_btn=Button(root2,text="Quit",bd=5,command=root2.destroy,padx=30).pack(pady=5)

    except Exception as e:
        print(e)
        root2.destroy()
        api="Error : "
        l2=Label(root,text= f"{api} \n {e} ", padx=10,pady=10,bg="white", fg="red")
        l2.grid(row=4,column=0,padx=10,pady=10)
        


my_img=ImageTk.PhotoImage(Image.open("images/4.jfif"))
my_label=Label(root, image=my_img,height=50,width=35)
my_label.grid(row=0,column=0,columnspan=2)                #the image is under the Movie App line

l2=Label(root,text="Movie App", font=("chiller", 70),bg="lightblue")
l2.grid(row=0,column=0,columnspan=2,pady=20)

e1=Entry(root,bd=2)
e1.grid(row=1,column=1,padx=10,pady=20)

l1=Label(root,text="IMDB Id", padx=10,pady=10,bg="lightblue")
l1.grid(row=1,column=0,padx=10,pady=20)

button=Button(root, text="Submit", command=fun,bd=5, padx=32)
button.grid(row=2,column=0,columnspan=2,pady=20)

quit_btn=Button(root,text="Quit",bd=5,command=root.quit, fg="red", bg="white",padx=40).grid(row=3,column=0,pady=10,columnspan=2)

root.mainloop()