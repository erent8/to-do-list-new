import tkinter as tk
from tkinter import ttk

to_do_list = []

def add_task():
    task = task_entry.get()
    to_do_list.append({"task": task, "completed": False})
    tasks_text.delete("1.0", tk.END)
    show_tasks()
    task_entry.delete(0, tk.END)
    print("Göreviniz eklendi.")

def show_tasks():
    tasks_text.delete("1.0", tk.END)
    tasks_text.insert(tk.END, "Yapılacak görevler:\n")
    for index, task in enumerate(to_do_list, start=1):
        task_text = f"{index}. {task['task']}"
        if task["completed"]:
            task_text += " (Tamamlandı)"
        tasks_text.insert(tk.END, task_text + "\n")

def delete_task():
    task_index = task_entry.get()
    if task_index.isdigit() and 1 <= int(task_index) <= len(to_do_list):
        task_index = int(task_index)
        to_do_list.pop(task_index - 1)
        tasks_text.delete("1.0", tk.END)
        show_tasks()
        print("Görev başarıyla silindi.")
    else:
        print("Geçersiz görev numarası.")

def toggle_task():
    task_index = task_entry.get()
    if task_index.isdigit() and 1 <= int(task_index) <= len(to_do_list):
        task_index = int(task_index)
        task = to_do_list[task_index - 1]
        task["completed"] = not task["completed"]
        tasks_text.delete("1.0", tk.END)
        show_tasks()
        print("Görev durumu güncellendi.")
    else:
        print("Geçersiz görev numarası.")

root = tk.Tk()
root.title("To-Do List")

# Arka plan rengini ayarlamak için bir çerçeve (frame) kullanalım
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Arka plan rengini ayarlayalım
style = ttk.Style()
style.configure("TFrame", background="#dcdcdc")

task_entry = tk.Entry(frame)
task_entry.pack(pady=5)

add_button = tk.Button(frame, text="Görev Ekle", command=add_task)
add_button.pack(pady=5)

tasks_text = tk.Text(frame)
tasks_text.pack(pady=5)

delete_button = tk.Button(frame, text="Görev Sil", command=delete_task)
delete_button.pack(pady=5)

toggle_button = tk.Button(frame, text="Görev Tamamlandı", command=toggle_task)
toggle_button.pack(pady=5)

root.mainloop()