from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("500x500")

my_tree=ttk.Treeview(root)
my_tree.pack()

#define columns
my_tree['columns']=("Name", "ID", "F.Pizza")
#formatting the columns
my_tree.column("#0", width=80, minwidth=10)
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
    ['0', "John1", 6, "pepperoni1"],
    ['1', "John2", 7, "pepperoni2"],
    ['5', "John3", 8, "pepperoni3"],
    ['4', "John4", 9, "pepperoni4"],
    ['7', "John5", 10, "pepperoni5"],
    ['8', "John6", 11, "pepperoni6"],
    ['8', "John7", 12, "pepperoni7"],
    ['', "John8", 13, "pepperoni8"],
    ['', "John9", 14, "pepperoni9"],
    ['', "John10", 15, "pepperoni10"]

]

count=0

for record in data:
    my_tree.insert(parent=record[0], index="end", iid=count, text="", values=(record[1], record[2], record[3]))
    count+=1

root.mainloop()

#fantom column is necessary for parent-child thing