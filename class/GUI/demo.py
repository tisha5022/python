from tkinter import *

import mysql.connector as sql
root = Tk()
root.geometry("700x500")



def insert():
    name =  e1.get()
    email = e2.get()
    phone = e3.get()

    con =sql.connect(
        host="127.0.0.1",
        user = "root",
        password = "root",
        port =3306,
        database="pythonsql"
    )
    cursor = con.cursor()
    cursor.execute(f"insert into emp values(0,'{name}','{email}','{phone}')")
    con.commit()
    print("data inserted")
  

l1 = Label(root,text="name").place(x=200,y=100)
l2 = Label(root,text="email").place(x=200,y=150)
l3 = Label(root,text="phone").place(x=200,y=200)

e1 = Entry(root).place(x=300,y=100)
e2 = Entry(root).place(x=300,y=150)
e3 = Entry(root).place(x=300,y=200)
e1 = Entry(root)
e1.place(x=300,y=100)
e2 = Entry(root)
e2.place(x=300,y=150)
e3 = Entry(root)
e3.place(x=300,y=200)

b1  =Button(root,text="submit",width=15).place(x=300,y=230)
b1  =Button(root,text="submit",command=insert,width=15).place(x=300,y=230)

root.mainloop()