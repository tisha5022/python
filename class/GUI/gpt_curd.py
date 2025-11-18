import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox  
import mysql.connector

# --- Database Connection ---
def connect_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",       # change if needed
        password="root",       # change if needed
        database="pythonsql"
    )

# --- Main Window ---
root = ttk.Window(themename="sandstone")  # try "darkly", "superhero", "flatly"
root.title("Employee Management Dashboard")
root.geometry("850x550")

# --- Gradient Header (using Frame + Label) ---
header = ttk.Frame(root, bootstyle="primary")
header.pack(fill="x")
ttk.Label(
    header,
    text="💼 Employee Management System",
    font=("Helvetica", 22, "bold"),
    bootstyle="inverse-primary",
    anchor="center",
    padding=15
).pack(fill="x")

# --- Input Frame ---
input_frame = ttk.Frame(root, padding=20)
input_frame.pack(fill="x")

# Variables
name_var = ttk.StringVar()
email_var = ttk.StringVar()
phone_var = ttk.StringVar()

# Input fields
ttk.Label(input_frame, text="Name:", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_entry = ttk.Entry(input_frame, textvariable=name_var, width=30, bootstyle="info")
name_entry.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(input_frame, text="Email:", font=("Segoe UI", 11, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
email_entry = ttk.Entry(input_frame, textvariable=email_var, width=30, bootstyle="info")
email_entry.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(input_frame, text="Phone:", font=("Segoe UI", 11, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
phone_entry = ttk.Entry(input_frame, textvariable=phone_var, width=30, bootstyle="info")
phone_entry.grid(row=2, column=1, padx=10, pady=10)

# --- Button Functions ---
def clear_fields():
    name_var.set("")
    email_var.set("")
    phone_var.set("")

def insert_data():
    if name_var.get() == "" or email_var.get() == "" or phone_var.get() == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO emp (name, email, phone) VALUES (%s, %s, %s)", 
                (name_var.get(), email_var.get(), phone_var.get()))
    conn.commit()
    conn.close()
    fetch_data()
    clear_fields()
    messagebox.showinfo("Success", "Employee added successfully!")

def fetch_data():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM emp")
    rows = cur.fetchall()
    emp_table.delete(*emp_table.get_children())
    for row in rows:
        emp_table.insert("", "end", values=row)
    conn.close()

def get_selected_row(event):
    selected = emp_table.focus()
    if not selected:
        return
    data = emp_table.item(selected)['values']
    if data:
        name_var.set(data[1])
        email_var.set(data[2])
        phone_var.set(data[3])

def update_data():
    selected = emp_table.focus()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a record to update!")
        return
    data = emp_table.item(selected)['values']
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE emp SET name=%s, email=%s, phone=%s WHERE id=%s",
                (name_var.get(), email_var.get(), phone_var.get(), data[0]))
    conn.commit()
    conn.close()
    fetch_data()
    clear_fields()
    messagebox.showinfo("Updated", "Record updated successfully!")

def delete_data():
    selected = emp_table.focus()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a record to delete!")
        return
    data = emp_table.item(selected)['values']
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete?")
    if confirm:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM emp WHERE id=%s", (data[0],))
        conn.commit()
        conn.close()
        fetch_data()
        clear_fields()
        messagebox.showinfo("Deleted", "Record deleted successfully!")

# --- Buttons Frame ---
btn_frame = ttk.Frame(root, padding=10)
btn_frame.pack()

ttk.Button(btn_frame, text="➕ Add", bootstyle="success", width=12, command=insert_data).grid(row=0, column=0, padx=8)
ttk.Button(btn_frame, text="✏ Update", bootstyle="warning", width=12, command=update_data).grid(row=0, column=1, padx=8)
ttk.Button(btn_frame, text="🗑 Delete", bootstyle="danger", width=12, command=delete_data).grid(row=0, column=2, padx=8)
ttk.Button(btn_frame, text="🧹 Clear", bootstyle="secondary", width=12, command=clear_fields).grid(row=0, column=3, padx=8)
ttk.Button(btn_frame, text="🔄 Refresh", bootstyle="info", width=12, command=fetch_data).grid(row=0, column=4, padx=8)

# --- Table Frame ---
table_frame = ttk.Frame(root, padding=10)
table_frame.pack(fill="both", expand=True)

columns = ("id", "name", "email", "phone")
emp_table = ttk.Treeview(table_frame, columns=columns, show="headings", bootstyle="info")
for col in columns:
    emp_table.heading(col, text=col.capitalize())
    emp_table.column(col, width=180, anchor="center")

emp_table.pack(fill="both", expand=True)
emp_table.bind("<ButtonRelease-1>", get_selected_row)

# Scrollbar
scroll_y = ttk.Scrollbar(emp_table, orient="vertical", command=emp_table.yview)
emp_table.configure(yscroll=scroll_y.set)
scroll_y.pack(side="right", fill="y")

# Load data initially
fetch_data()

root.mainloop()