from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as sql

con = sql.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    port =3306,
    database="pythonsql"
)

root = Tk()
root.geometry("700x500")


def show():
    cursoer = con.cursor()
    cursoer.execute("select * from emp")
    data = cursoer.fetchall()
    for i,(id,name,email,phone) in enumerate(data,start=1):
        table.insert("",END,values=(id,name,email,phone))

def adddata():
    name = e1.get()
    email=e2.get()
    phone=e3.get()
    cursor = con.cursor()
    qry = "insert into emp values(%s,%s,%s,%s)"
    val = (0,name,email,phone)
    cursor.execute(qry,val)  
    con.commit() 
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e1.focus()
    for i in table.get_children():
        table.delete(i)
    show()
    messagebox.showinfo("Success","Data inserted")

id = 0
def getdata(self):
    global id
    rowid = table.selection()[0]
    data = table.set(rowid)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    id = data['ID']
    e1.insert(0,data['Name'])
    e2.insert(0,data['Email'])
    e3.insert(0,data['Phone'])

def deletedata():
    cursor = con.cursor()
    cursor.execute(f"delete from emp where id={id}")
    con.commit()
    for i in table.get_children():
        table.delete(i)
    show()

def updatedata():
    name = e1.get()
    email=e2.get()
    phone=e3.get()
    cursor = con.cursor()
    qry = "update emp set name=%s,email=%s,phone=%s where id=%s"
    val = (name,email,phone,id)
    cursor.execute(qry,val)  
    con.commit() 
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e1.focus()
    for i in table.get_children():
        table.delete(i)
    show()

l1 = Label(root,text="Name").place(x=200,y=50)
l2 = Label(root,text="Email").place(x=200,y=80)
l3 = Label(root,text="Phone").place(x=200,y=110)

e1 = Entry(root)
e1.place(x=270,y=50)
e2 = Entry(root)
e2.place(x=270,y=80)
e3 = Entry(root)
e3.place(x=270,y=110)

b1 = Button(text="ADD",command=adddata,width=7).place(x=200,y=140)
b2 = Button(text="UPDATE",command=updatedata,width=7).place(x=270,y=140)
b3 = Button(text="DELETE",command=deletedata,width=7).place(x=340,y=140)

cols = ("ID","Name","Email","Phone")
table = ttk.Treeview(root,columns=cols,show="headings")
for col in cols:
    table.heading(col,text=col)
    table.place(x=10,y=190)

show()

table.bind("<Double-Button-1>",getdata)

root.mainloop()