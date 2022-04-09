from tkinter import *
from tkinter import messagebox
import shelve


def handleError(task):
    if task == "":
        messagebox.showwarning("warning", "Please enter a task.")
    else:
        messagebox.showwarning("warning", "Task already exists")


def newTask():
    task = my_entry.get()
    sh = shelve.open("tasks")
    if task != "" and task not in sh:
        lb.insert(END, task)
        my_entry.delete(0, "end")
        sh[task] = task
    else:
        handleError(task)


def deleteTask():
    sh = shelve.open("tasks")
    print(lb.get(ANCHOR))
    del sh[lb.get(ANCHOR)]
    lb.delete(ANCHOR)


if __name__ == "__main__":
    ws = Tk()
    ws.geometry('500x450+500+200')
    ws.title('Task manager')
    ws.config(bg='#223441')
    ws.resizable(width=False, height=False)

    frame = Frame(ws)
    frame.pack(pady=10)

    lb = Listbox(
        frame,
        width=25,
        height=8,
        font=('Times', 18),
        bd=0,
        fg='#464646',
        highlightthickness=0,
        selectbackground='#a6a6a6',
        activestyle="none",

    )
    lb.pack(side=LEFT, fill=BOTH)

    sh = shelve.open("tasks")
    for texts in sh:
        lb.insert(END, sh[texts])

    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)

    lb.config(yscrollcommand=sb.set)
    sb.config(command=lb.yview)

    my_entry = Entry(
        ws,
        font=('times', 24)
    )

    my_entry.pack(pady=20)

    button_frame = Frame(ws)
    button_frame.pack(pady=20)

    addTask_btn = Button(
        button_frame,
        text='Add Task',
        font=('times 14'),
        bg='#c5f776',
        padx=20,
        pady=10,
        command=newTask
    )
    addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

    delTask_btn = Button(
        button_frame,
        text='Delete Task',
        font=('times 14'),
        bg='#ff8b61',
        padx=20,
        pady=10,
        command=deleteTask
    )
    delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


    ws.mainloop()