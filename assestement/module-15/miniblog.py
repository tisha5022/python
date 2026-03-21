import tkinter as tk
from tkinter import messagebox
import os

class User:
    def __init__(self, name):
        self.name = name

class Post:
    def __init__(self, user, title, content):
        self.user = user
        self.title = title
        self.content = content

    def save_post(self):
        filename = f"{self.user.name}_{self.title}.txt"
        with open(filename, "w") as file:
            file.write("Author: " + self.user.name + "\n")
            file.write("Title: " + self.title + "\n\n")
            file.write(self.content)

def save_post():
    name = name_entry.get()
    title = title_entry.get()
    content = content_text.get("1.0", tk.END)

    if name == "" or title == "" or content.strip() == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        user = User(name)
        post = Post(user, title, content)
        post.save_post()
        messagebox.showinfo("Success", "Post Saved Successfully!")
        load_posts()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def load_posts():
    post_list.delete(0, tk.END)
    for file in os.listdir():
        if file.endswith(".txt"):
            post_list.insert(tk.END, file)

def view_post():
    try:
        selected = post_list.get(post_list.curselection())
        with open(selected, "r") as file:
            data = file.read()

        content_text.delete("1.0", tk.END)
        content_text.insert(tk.END, data)
    except:
        messagebox.showerror("Error", "Please select a post")

root = tk.Tk()
root.title("MiniBlog Application")
root.geometry("600x500")

tk.Label(root, text="User Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Post Title").pack()
title_entry = tk.Entry(root, width=40)
title_entry.pack()

tk.Label(root, text="Post Content").pack()
content_text = tk.Text(root, height=10, width=50)
content_text.pack()

tk.Button(root, text="Save Post", command=save_post).pack(pady=5)
tk.Button(root, text="View Post", command=view_post).pack(pady=5)

tk.Label(root, text="Saved Posts").pack()

post_list = tk.Listbox(root, width=50)
post_list.pack()

load_posts()

root.mainloop()