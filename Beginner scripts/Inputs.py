import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("My Inputs App")
root.geometry("500x400")
def clearwindow():
    for widget in root.winfo_children():
        widget.destroy()
def add_new_content():
    tk.Label(root,text="Welcome!").pack(pady=20)
def submit():
    name = name_entry.get()
    age = age_entry.get()  


    if name == '' or age == '':
        messagebox.showerror("Input Error", "Please insert your name and age!")
    else:
        try:
            age = int(age)
            if age > 17:
                messagebox.showinfo("Welcome", f"Hello,{name}! You are old enough to use my app!")
                clearwindow()
                add_new_content()
            else:
                messagebox.showwarning("Age Restriction", "You have to be 18+ to use this app!")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid age!")


tk.Label(root, text="Name:").pack(pady=10)
name_entry = tk.Entry(root)
name_entry.pack(pady=10)

tk.Label(root, text="Enter Age:").pack(pady=10)
age_entry = tk.Entry(root)
age_entry.pack(pady=10)

tk.Button(root, text="Submit", command=submit).pack(pady=20)

root.mainloop()
