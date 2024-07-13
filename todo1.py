# TO DO LIST APPLICATION
import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        tk.messagebox.showwarning(title="Warning", message="Please enter a task.")


def update_task():
    selected_task = listbox.curselection()
    if selected_task:
        task = entry.get()
        listbox.delete(selected_task)
        listbox.insert(selected_task[0], task)
        entry.delete(0, tk.END)
    else:
        tk.messagebox.showwarning(title="Warning",message="Please select a task to update.")

def delete_task():
    selected_task = listbox.curselection()[0]
    if selected_task:
        listbox.delete(selected_task)
    else:
        tk.messagebox.showwarning(title="Warning", message="Please select a task to delete.")


root = tk.Tk()
root.title('To-Do List')
root.config(bg="grey")
root.geometry('800x200')

entry = tk.Entry(root,width=90)
entry.pack()

add_button = tk.Button(root, text='Add Task',width=90, command=add_task)
add_button.pack()

update_button = tk.Button(root, text='Update Task',width=90, command=update_task)
update_button.pack()

delete_button = tk.Button(root, text='Delete Task',width=90, command=delete_task)
delete_button.pack()

listbox = tk.Listbox(root,width=90)
listbox.pack()

root.mainloop()
