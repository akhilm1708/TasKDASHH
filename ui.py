import tkinter as tk
from tkinter import messagebox
import requests
from funcs import *

API = "https://cs-api.pltw.org/"
user = "tasks"

def post_task():
    task_text = post_entry.get()
    
    if not task_text:
        messagebox.showerror("Error", "Please enter a task.")
        return
    
    try:
        url = API + user + "?text=" + task_text
        response = requests.post(url)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Task posted successfully!")
        else:
            messagebox.showerror("Error", f"Failed to post task: {response.text}")
    
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def get_tasks():
    try:
        url = API + user
        response = requests.get(url)

        if response.status_code == 200:
            tasks = response.json()

            if "strings" in tasks and "values" in tasks:
                # searched zip up lol, it can iterate through both parsed sections at once
                tasks_list = "\n".join([f"Task: {task}, Priority: {priority}" for task, priority in zip(tasks["strings"], tasks["values"])])
                # print(tasks_list)

                messagebox.showinfo("Tasks", tasks_list)
            else:
                messagebox.showerror("Error", "No tasks or values found in the response.")
        else:
            messagebox.showerror("Error", f"Failed to retrieve tasks: {response.text}")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")




def increment_priority():
    try:
        task_id = task_id_entry.get()  
        priority_increase = int(priority_entry.get())  #  how much to increase the priority
        
        if not task_id or priority_increase <= 0:
            messagebox.showerror("Error", "Please provide a valid task ID and priority increase.")
            return

        url = API + user + "/increment?id=" + task_id
        for _ in range(priority_increase):
            response = requests.post(url)
            if response.status_code != 200:
                messagebox.showerror("Error", f"Failed to increment priority: {response.text}")
                return
        
        messagebox.showinfo("Success", f"Priority of Task {task_id} increased by {priority_increase}.")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for priority increase.")

def clear_tasks():
    task_delete = clear_entry.get()
    
    if not task_delete:
        messagebox.showerror("Error", "Please enter a task.")
        return
    
    try:
        url = API + user + "/reset?password=" + task_delete
        response = requests.post(url)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Tasks cleared successfully!")
        else:
            messagebox.showerror("Error", f"Failed to clear tasks: {response.text}")
    
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def create_ui():
    global post_entry, task_id_entry, clear_entry, priority_entry
    
    root = tk.Tk()
    root.title("TasKDASH")
    root.geometry("400x300")
    root.resizable(True, True)
    # root.resizable(False, False)
    root.configure(bg="lightblue")

    tk.Label(root, text="To-Do List App", font=("Arial", 16, "bold")).pack(pady=10)
    
    frame = tk.Frame(root)
    frame.pack(pady=5)
    
    post_frame = tk.Frame(root, relief="solid", bd=2, padx=10, pady=10)
    post_frame.pack(padx=10, pady=10, fill="x")

    tk.Label(post_frame, text="Enter Task to Post:").pack(side=tk.LEFT)
    post_entry = tk.Entry(post_frame, width=40)
    post_entry.pack(side=tk.LEFT)

    post_button = tk.Button(post_frame, text="Post Task", width=20, command=post_task)
    post_button.pack(pady=10)

    clear_frame = tk.Frame(root, relief="solid", bd=2, padx=10, pady=10)
    clear_frame.pack(padx=10, pady=15, fill="x")

    clear_button = tk.Button(clear_frame, text="Clear Tasks (enter password)", width=25, command=clear_tasks)
    clear_button.pack(pady=5, padx=10, side=tk.LEFT)

    clear_entry = tk.Entry(clear_frame, width=40)
    clear_entry.pack(side = tk.LEFT)

    increment_frame = tk.Frame(root, relief="solid", bd=2, padx=10, pady=10)
    increment_frame.pack(padx=10, pady=20, fill="x")

    tk.Label(increment_frame, text="Task ID to Increment Priority:").pack(pady=5)
    task_id_entry = tk.Entry(increment_frame, width=40)
    task_id_entry.pack(pady=5)

    tk.Label(increment_frame, text="Priority Increase (Number):").pack(pady=5)
    priority_entry = tk.Entry(increment_frame, width=40)
    priority_entry.pack(pady=5)

    increment_button = tk.Button(increment_frame, text="Increment Priority", width=20, command=increment_priority)
    increment_button.pack(pady=10)

    get_button = tk.Button(root, text="Get Tasks", width=20, command=get_tasks)
    get_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", width=20, fg="red", command=root.quit)
    exit_button.pack(pady=30)

    root.mainloop()


#testing w/out main.py
# create_ui()
