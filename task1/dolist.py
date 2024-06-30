import tkinter as tk
from tkinter import messagebox
import json
class Task:
    def __init__(self, task, due_date, priority):
        self.description, self.due_date, self.priority = task, due_date, priority
    def to_dict(self):
        return {"description": self.description, "due_date": self.due_date, "priority": self.priority}
    def from_dict(data):
        return Task(data["description"], data["due_date"], data["priority"])
def view_tasks():
    task_list.delete(0, tk.END)
    [task_list.insert(tk.END, f"{i+1}. Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}") for i, task in enumerate(tasks)]
def add_or_update_task():
    try:
        index = task_list.curselection()[0]
        tasks[index] = Task(description_entry.get(), due_date_entry.get(), priority_entry.get())
    except IndexError:
        tasks.append(Task(description_entry.get(), due_date_entry.get(), priority_entry.get()))
    save_tasks()
    view_tasks()
    clear_entries()
def delete_task():
    try:
        del tasks[task_list.curselection()[0]]
        save_tasks()
        view_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump([task.to_dict() for task in tasks], file)
def clear_entries():
    description_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)
try:
    with open("tasks.json", "r") as file:
        tasks = [Task.from_dict(task_data) for task_data in json.load(file)]
except FileNotFoundError:
    tasks = []
root = tk.Tk()
root.title("To-Do List")
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)
tk.Label(frame, text="Task:").grid(row=0, column=0, sticky="e")
tk.Label(frame, text="Due Date:").grid(row=1, column=0, sticky="e")
tk.Label(frame, text="Priority:").grid(row=2, column=0, sticky="e")

description_entry = tk.Entry(frame)
description_entry.grid(row=0, column=1)
due_date_entry = tk.Entry(frame)
due_date_entry.grid(row=1, column=1)
priority_entry = tk.Entry(frame)
priority_entry.grid(row=2, column=1)

tk.Button(frame, text="Add/Update Task", command=add_or_update_task).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(frame, text="Delete Task", command=delete_task).grid(row=4, column=0, columnspan=2, pady=5)

task_list = tk.Listbox(frame, width=100)
task_list.grid(row=15, column=0, columnspan=2, pady=10)

view_tasks()
root.mainloop()
