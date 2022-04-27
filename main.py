from tkinter import *
from tkinter import messagebox
import shelve


class GUI():
    def __init__(self):
        self.ws = Tk()
        self.ws.geometry('500x450+500+200')
        self.ws.title('Task manager')
        self.ws.config(bg='#223441')
        self.ws.resizable(width=False, height=False)

        self.frame = Frame(self.ws)
        self.frame.pack(pady=10)

        self.lb = Listbox(
            self.frame,
            width=25,
            height=8,
            font=('Times', 18),
            bd=0,
            fg='#464646',
            highlightthickness=0,
            selectbackground='#a6a6a6',
            activestyle="none",

        )
        self.lb.pack(side=LEFT, fill=BOTH)

        sh = shelve.open("tasks")
        for texts in sh:
            self.lb.insert(END, sh[texts])

        self.sb = Scrollbar(self.frame)
        self.sb.pack(side=RIGHT, fill=BOTH)

        self.lb.config(yscrollcommand=self.sb.set)
        self.sb.config(command=self.lb.yview)

        self.my_entry = Entry(
            self.ws,
            font=('times', 24)
        )

        self.my_entry.pack(pady=20)

        self.button_frame = Frame(self.ws)
        self.button_frame.pack(pady=20)

        self.addTask_btn = Button(
            self.button_frame,
            text='Add Task',
            font=('times 14'),
            bg='#c5f776',
            padx=20,
            pady=10,
            command=self.newTask
        )
        self.addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

        self.delTask_btn = Button(
            self.button_frame,
            text='Delete Task',
            font=('times 14'),
            bg='#ff8b61',
            padx=20,
            pady=10,
            command=self.deleteTask
        )
        self.delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)
        self.ws.mainloop()

    def handleError(self, task):
        if task == "":
            messagebox.showwarning("warning", "Please enter a task.")
        else:
            messagebox.showwarning("warning", "Task already exists")

    def newTask(self):
        task = self.my_entry.get()
        sh = shelve.open("tasks")
        if task != "" and task not in sh:
            self.lb.insert(END, task)
            self.my_entry.delete(0, "end")
            sh[task] = task
        else:
            self.handleError(task)

    def deleteTask(self):
        sh = shelve.open("tasks")
        del sh[self.lb.get(ANCHOR)]
        self.lb.delete(ANCHOR)


if __name__ == "__main__":
    GUI()

