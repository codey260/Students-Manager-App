import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, simpledialog
import json
import os

class App:
  def __init__(self, master):
    self.master = master
    self.master.title("Students Manager")
    self.master.geometry("320x335") # Phone Friendly Size

    # Create UI Elements
    self.create_widgets()

    # Data File
    self.data_file = "data.json"
    self.students = self.load_students()

    # Refreshing Listbox
    self.refresh_listbox()
  
  def load_students(self):
    if os.path.exists(self.data_file):
      with open(self.data_file, "r") as file:
        try:
          return json.load(file)
        except json.JSONDecodeError:
          return []
    
    return []
  
  def save_students(self):
    with open(self.data_file, "w") as file:
      json.dump(self.students, file, indent=4)

  def create_widgets(self):
      # Title Label
      title = tk.Label(self.master, text="Students Manager", font=("Helvetica", 18, "bold"))
      title.pack(pady=5)

      # Student Name Entry
      self.entry_var = tk.StringVar()
      entry_frame = tk.Frame(self.master)
      entry_frame.pack(pady=5)

      entry_label = tk.Label(entry_frame, text="Student Name:", font=("Helvetica", 12))
      entry_label.pack(side=tk.LEFT)

      entry = tk.Entry(entry_frame, textvariable=self.entry_var, font=("Helvetica", 12), width=30)
      entry.pack(side=tk.LEFT)

      # Buttons Frame
      buttons_frame = tk.Frame(self.master)
      buttons_frame.pack(pady=5)

      add_btn = tk.Button(buttons_frame, text="Add Student", command=self.add_student, width=10)
      add_btn.grid(row=0, column=0)

      remove_btn = tk.Button(buttons_frame, text="Remove Student", command=self.remove_student, width=10)
      remove_btn.grid(row=0, column=1)

      check_btn = tk.Button(buttons_frame, text="Check Student", command=self.check_student, width=10)
      check_btn.grid(row=0, column=2)

      clear_btn = tk.Button(buttons_frame, text="Clear All", command=self.clear_students,  width=10)
      clear_btn.grid(row=1, column=0)

      update_btn = tk.Button(buttons_frame, text="Update Student", command=self.update_student,  width=10)
      update_btn.grid(row=1, column=1)

      exit_btn = tk.Button(buttons_frame, text="Exit", command=self.master.quit, width=10)
      exit_btn.grid(row=1, column=2)

      # Students Listbox
      list_frame = tk.Frame(self.master)
      list_frame.pack(pady=5, fill=tk.BOTH, expand=True)

      self.listbox = Listbox(list_frame, font=("Helvetica", 12), width=40, height=20)
      self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

      scrollbar = Scrollbar(list_frame, command=self.listbox.yview)
      scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
      self.listbox.config(yscrollcommand=scrollbar.set)

  
  def add_student(self):
    name = self.entry_var.get().strip().title()
    if not name:
        messagebox.showwarning("Input Error", "Please enter a student name.")
        return
    if name in self.students:
        messagebox.showinfo("Duplicate", f"{name} is already in the list.")
        return
    self.students.append(name)
    self.save_students()
    self.refresh_listbox()
    self.entry_var.set("")
  
  def remove_student(self):
    selected = self.listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a student to remove.")
        return
    name = self.listbox.get(selected)
    self.students.remove(name)
    self.save_students()
    self.refresh_listbox()
  
  def check_student(self):
    name = self.entry_var.get().strip().title()
    if not name:
        messagebox.showwarning("Input Error", "Please enter a student name to check.")
        return
    if name in self.students:
        messagebox.showinfo("Found", f"Student {name} is in the list.")
    else:
        messagebox.showinfo("Not Found", f"Student {name} not found.")
  
  def update_student(self):
    selected = self.listbox.curselection()
    
    if not selected:
        messagebox.showwarning("Selection error", "Please select a student to update")
    
    if selected:
        old_name = self.listbox.get(selected)
        new_name = simpledialog.askstring("Update Student", f"Enter new name for {old_name}:")
        if new_name:
            new_name = new_name.strip().title()

        if not new_name:
                messagebox.showwarning("Input Error", "New name cannot be empty")
                return
        if new_name in self.students:
                messagebox.showwarning("Duplicate", f"Student {new_name} is already in the list")
                return
        index = self.students.index(old_name)
        self.students[index] = new_name
        self.save_students()
        self.refresh_listbox()

  def clear_students(self):
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to clear all students?")
    if confirm:
        self.students.clear()
        self.save_students()
        self.refresh_listbox()
 

  def refresh_listbox(self):
    self.listbox.delete(0, tk.END)
    for student in sorted(self.students):
        self.listbox.insert(tk.END, student)

if __name__ == "__main__":
  root = tk.Tk()
  app = App(root)
  root.mainloop()
