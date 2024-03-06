import tkinter as tk
import tkinter.messagebox as messagebox



def open_add_task_window():
    def add_task():
        with open("task_list", "a") as file:
            task_value = entry_area.get("1.0", "end-1c")
            file.write(f"{task_value}\n")
            messagebox.showinfo("Task added", "Your task has been added successfully!")
            

         
            
    def clear():
        entry_area.delete("1.0", "end")

    add_task_window = tk.Toplevel(root)
    add_task_window.title("Add Task")
    add_task_window.geometry("600x310")
    add_task_window.minsize(600, 310)
    add_task_window.maxsize(600, 310)
    entry_area = tk.Text(add_task_window, width=50, height=10, font=("Courier", 13))
    entry_area.pack(pady=30)
    button_frame = tk.Frame(add_task_window, padx=10)
    button_frame.pack(side="top")
    tk.Button(button_frame, text="Add Task", width=15, borderwidth=3, command=add_task).pack(side="left")
    tk.Button(button_frame, text="Clear", width=15, borderwidth=3, command=clear).pack(side="left")


root = tk.Tk()
root.title("Todo Application")
root.geometry("700x400")
root.minsize(450, 400)
root.maxsize(700, 400)

tk.Label(text="This is a Task Manager", bg="grey", fg="white", borderwidth=3, relief="groove", font=("Courier New Baltic", 10, "bold"),padx=50, pady=15).pack(side="top")
f1 = tk.Frame(root, borderwidth=3, relief="ridge")
f1.pack(side="top", pady=20)
tk.Button(f1, text="Add Task", padx=50, width=15, borderwidth=3, font=("Courier New Baltic", 10), command=open_add_task_window).pack(pady=20, padx=95)
tk.Button(f1, text="Remove task", padx=50, width=15, borderwidth=3, font=("Courier New Baltic", 10)).pack(pady=20)
tk.Button(f1, text="Task List", padx=50, width=15, borderwidth=3, font=("Courier New Baltic", 10)).pack(pady=20)
tk.Button(f1, text="Exit", padx=50, width=15, borderwidth=3, font=("Courier New Baltic", 10), command=root.destroy).pack(pady=20)


root.mainloop()