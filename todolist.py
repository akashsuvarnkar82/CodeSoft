from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("To-Do List Application")
root.geometry("400x500")
root.configure(bg="#F7F9FF")

tasks = []

h_frame = Frame(root, bg="#F7F9FF")
h_frame.pack(pady=20)

h_label = Label(h_frame, text="To-Do List App", font=("Ubuntu", 16, "bold"), bg="#F7F9FF", fg="#333333")
h_label.pack()

entry_frame = Frame(root, bg="#F7F9FF")
entry_frame.pack(pady=10)

task_entry = Entry(entry_frame, width=30, font=("Arial", 12), bd=0, relief="flat", highlightthickness=2, highlightcolor="#E8E8E8")
task_entry.grid(row=0, column=0, padx=10)

task_listbox = Listbox(root, height=10, width=40, font=("Arial", 12), bg="#F7F9FF", fg="#333333", bd=0, selectbackground="#FF6B6B")
task_listbox.pack(pady=20)

button_frame = Frame(root, bg="#F7F9FF")
button_frame.pack()


#Adding the task in tasks list
def update_listbox():
    task_listbox.delete(0, END)
    for task in tasks:
        task_listbox.insert(END, task)
        
def add_task():
    task = task_entry.get()
    if task != "":
        index = len(tasks) + 1
        task_with_index = f"{index}. {task}"
        tasks.append(task_with_index)
        update_listbox()
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")
        
add_button = Button(entry_frame, text="ADD", command=add_task, width=10, bg="#FF6B6B", fg="white", font=("Arial", 12, "bold"), bd=0, relief="flat")
add_button.grid(row=0, column=1)




#Remove the task in tasks list
def remove_task():
    try:
        task_index = task_listbox.curselection()[0]
        tasks.pop(task_index)  
        for i in range(len(tasks)):
            tasks[i] = f"{i+1}. {tasks[i].split('. ', 1)[1]}"
        update_listbox() 
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

remove_button = Button(button_frame, text="Remove Task", command=remove_task, width=15, bg="#FFC107", fg="white", font=("Arial", 12, "bold"), bd=0, relief="flat")
remove_button.grid(row=0, column=0, padx=10, pady=10)



#To mark the task is completed 
def complete_task():
    try:
        task_index = task_listbox.curselection()[0]
        completed_task = tasks[task_index] + " (Completed)"
        tasks[task_index] = completed_task
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

complete_button = Button(button_frame, text="Mark Completed", command=complete_task, width=15, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), bd=0, relief="flat")
complete_button.grid(row=0, column=1, padx=10, pady=10)


#Clear all task in tasks list
def clear_tasks():
    global tasks
    tasks = []
    update_listbox()

clear_button = Button(button_frame, text="Clear All", command=clear_tasks, width=15, bg="#FF5252", fg="white", font=("Arial", 12, "bold"), bd=0, relief="flat")
clear_button.grid(row=1, column=0, columnspan=2, pady=10)


root.mainloop()

