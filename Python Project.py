# Simple To-Do List App

import tkinter as tk
from tkinter import messagebox

# ---------- Functions (what the buttons do) ----------

def add_task():
    task = entry.get()                      # read what the user typed
    if task == "":
        messagebox.showwarning("Oops", "Please type a task.")
    else:
        listbox.insert(tk.END, task)        # add it to the list
        entry.delete(0, tk.END)             # clear the text box


def delete_task():
    selected = listbox.curselection()       # which task is selected?
    if selected:
        listbox.delete(selected[0])         # remove it
    else:
        messagebox.showinfo("Info", "Click a task first.")


def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.itemconfig(index, fg="gray")   # turn the task gray
    else:
        messagebox.showinfo("Info", "Click a task first.")


# ---------- Window and widgets ----------

window = tk.Tk()
window.title("My To-Do List")
window.geometry("350x420")

title = tk.Label(window, text="My To-Do List", font=("Arial", 16, "bold"))
title.pack(pady=10)

entry = tk.Entry(window, width=30, font=("Arial", 12))
entry.pack(pady=5)

add_button = tk.Button(window, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(window, width=35, height=10, font=("Arial", 12))
listbox.pack(pady=10)

done_button = tk.Button(window, text="Mark Done", width=15, command=mark_done)
done_button.pack(pady=3)

delete_button = tk.Button(window, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=3)

# Keep the window open
window.mainloop()