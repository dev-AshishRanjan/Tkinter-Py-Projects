#treeview with style and theme
#striped treeview


from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("500x500")
root.title("Treeview : styles and themes")
root.configure(bg="silver")

#add some style

style=ttk.Style()
#adding themes
style.theme_use("clam")

style.configure("Treeview", background="#D3D3D3", foreground="red", rowheight=25, fieldbackground="#D3D3D3")
style.map("Treeview", background=[("selected", "pink")])

my_tree=ttk.Treeview(root)
my_tree.pack()

#define columns
my_tree['columns']=("Name", "ID", "F.Pizza")
#formatting the columns
my_tree.column("#0", width=0, minwidth=0, stretch=NO)
my_tree.column("Name", width=120, minwidth=20,anchor=W)
my_tree.column("ID", width=80, minwidth=20,anchor=CENTER)
my_tree.column("F.Pizza", width=120, minwidth=20,anchor=W)
#creating Headings
my_tree.heading("#0", text="Parents")
my_tree.heading("Name", text="Name",anchor=W)
my_tree.heading("ID", text="ID",anchor=CENTER)
my_tree.heading("F.Pizza", text="F.Pizza",anchor=W)

#adding data by loop method
data=[
    ['', "John", 1, "pepperoni"],
    ['', "Mary", 2, "Cheese"],
    ['', "Tim", 3, "mushroom"],
    ['', "Erin", 4, "ham"],
    ['', "Bob", 5, "onion"],
    ['', "John1", 6, "pepperoni1"]
]

#create striped row tags
my_tree.tag_configure("oddrow", background="white")
my_tree.tag_configure("evenrow", background="skyblue")

global count
count=0

for record in data:

    if count %2 ==0:
        my_tree.insert(parent=record[0], index="end", iid=count, text="", values=(record[1], record[2], record[3]), tags=("evenrow",))

    else:
        my_tree.insert(parent=record[0], index="end", iid=count, text="", values=(record[1], record[2], record[3]), tags=("oddrow",))
    
    count+=1

    #if count % 2 == 0:
    #    style.configure("Treeview",background="red", foreground="red", rowheight=25, fieldbackground="#D3D3D3")
    #  style.map("Treeview", background=[("selected", "pink")])
    #else:
    #    style.configure("Treeview",background="lightblue", foreground="red", rowheight=25, fieldbackground="#D3D3D3")
    #    style.map("Treeview", background=[("selected", "pink")])
    #elif count % 3 == 2 :
    #    style.configure("Treeview",background="pink", foreground="red", rowheight=25, fieldbackground="#D3D3D3")
    #    style.map("Treeview", background=[("selected", "pink")])


    # # # above commented way doesnot work


    
    
    

root.mainloop()

#fantom column is necessary for parent-child thing