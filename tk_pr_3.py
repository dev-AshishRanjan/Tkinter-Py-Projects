#  library = Tkinter
#  This project is based on tk_pr_2.py
#  In tk_pr_2.py , for invalid data (submit) is deactivated so you cannot submit further. But here it is active always

from tkinter import *
root= Tk()

e1=Entry(root, width=50, borderwidth=5)
e1.pack()
e1.insert(0,"Enter your Name")

e2=Entry(root, width=50, borderwidth=5, fg='red')
e2.pack()
e2.insert(0, "Enter your Email_id")

e3=Entry(root, width=50, borderwidth=5, fg='grey')
e3.pack()
e3.insert(0,"Enter your Work_Field")

def fun():
    if e1.get()=='' or e2.get()=='Enter your Email_id' or  e3.get()=='Enter your Work_Field':
        #but['state']= DISABLED
        Label(root, text='Enter Valid Data').pack()

    elif e1.get()=='Enter your Name' or e2.get()=='' or  e3.get()=='':
        #but['state']= DISABLED
        Label(root, text='Enter Valid Data').pack()
    else:
        l1= Label(root, text=f'Name: {e1.get()}').pack()
        l2= Label(root, text=f'Email_id: {e2.get()}').pack()
        l2= Label(root, text=f'Work_Field: {e3.get()}').pack()
        l=Label(root, text="Don't worry Your Data is Safe").pack()
        but=Button(root, text='Final  Submit', fg='green', command= fun2, state=ACTIVE).pack()

def fun2():
    l= Label(root,text="Thank You for using our Service \n This app is under work and hasn't finished \n \n Have a Nice Day ahead" ).pack()
    if e1.get()=='Ashish':
        l=Label(root,text="Hey are you our Dev because your name matches our Dev's name" ).pack()
        l=Label(root,text='\n KUMAR ASHISH RANJAN is our Developer \n\n\n\n' ).pack()




mybutton= Button(root, text= 'submit', borderwidth=5, bg='cyan', fg='red', command=fun, state=ACTIVE )
mybutton.pack()

root.mainloop()