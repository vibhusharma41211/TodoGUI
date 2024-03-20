import tkinter as tk
from tkinter import *

app = tk.Tk()
app.title("To-Do List App")
app.geometry("400x650+400+100")  # Set the size of the window
app.resizable(False,False)

tasks = []

def open_task_file():
    try:
        global tasks
        with open("taskfile.txt","r") as taskfile:
            task2 = taskfile.readlines()

        for task in task2:
            if task !='\n':
                tasks.append(task.strip()) #added .strip() to remove leading and trailing whitespace, including the newline character
                listbox.insert(END, task.strip())
    
    except:
        file=open("taskfile.txt", "w")
        file.close()

def add_task():
    task = entry_data.get()
    entry_data.delete(0,END)
    if task:
        with open("taskfile.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        tasks.append(task)
        listbox.insert(END, task)
        

def delete_task():
    global tasks
    task_index = listbox.curselection() #corrected the usage of listbox.get() and added logic to get the task at the selected index
    if task_index:
        task_index = task_index[0]
        task = listbox.get(task_index) #corrected the usage of listbox.get() and added logic to get the task at the selected index
        if task in tasks:
            tasks.remove(task)
            with open("taskfile.txt", "w" ) as taskfile:
                for task in tasks:
                    taskfile.write(task + "\n")
            update_listbox()

def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)


image_icon = PhotoImage(file="Py-todo/task.png") #Added top icon
app.iconphoto(False,image_icon)

top_bar = PhotoImage(file="Py-todo/topbar.png") #Added top bar
Label(app,image=top_bar).pack()

dock_image = PhotoImage(file="Py-todo/dock.png") #Added dock image at top left
Label(app,image=dock_image,bg="#32405b").place(x=30,y=25)

Label(app,image=image_icon, bg="#32405b").place(x=340, y=20) #Added Task image to the top right 

heading = Label(app, text="All Tasks", font="Calibri 20 bold italic", fg="White", bg="#32405b") #Added headline
heading.place(x=150, y=20)

#Entry section
label = tk.Label(app, text="Enter task:", font="Calibri 20 bold italic")
label.pack()

entry_frame = Frame(app, width=400, height=40, bg="White")
entry_frame.place(x=0,y=130)

entry_data = Entry(entry_frame, width=37, font="Calibri 15",) 
entry_data.place(x=10, y=7)
entry_data.focus()

#Add button creation
add_button = tk.Button(app, text="Add Task",width=20, font="Calibri 15 italic", bg="#93C47D", command=add_task)
add_button.place(x=100, y=180)

#Delete icon creation
delete_icon = PhotoImage(file="Py-todo/delete.png")
Button(app, image=delete_icon, bd=0, command=delete_task).pack(side=BOTTOM, pady=(13))

#List box
list_box_frame = Frame(app, bd=4, width=700, height=300, bg="#0B5394")
list_box_frame.pack(pady=(120,0))

listbox = Listbox(list_box_frame, font="Calibri 15", width=37, height=16, bg="#0B5394",fg="White", cursor="hand2", selectbackground="#5A95FF" )
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(list_box_frame, command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)

#Call a funtion to open task file so the data will remain same
open_task_file()

app.mainloop()