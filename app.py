from customtkinter import *
import json
import os

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("📚 Students Manager")
        self.master.geometry("800x500")
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

        self.data_file = "data.json"
        self.students = self.load_students()

        self.create_widgets()
        self.refresh_listbox()

    def load_students(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def save_students(self):
        with open(self.data_file, "w") as f:
            json.dump(self.students, f, indent=4)

    def create_widgets(self):
        CTkLabel(self.master, text="Students Manager", font=("Arial", 28, "bold")).pack(pady=10)

        # 🔔 Message label
        self.message_var = StringVar(value="")
        self.message_label = CTkLabel(self.master, textvariable=self.message_var, text_color="white", font=("Arial", 14))
        self.message_label.pack(pady=(0, 5))

        # Entry Section
        entry_frame = CTkFrame(self.master, fg_color="transparent")
        entry_frame.pack(pady=10)

        CTkLabel(entry_frame, text="Name:", font=("Arial", 16)).pack(side=LEFT, padx=10)

        self.entry_var = StringVar()
        self.entry = CTkEntry(entry_frame, textvariable=self.entry_var, placeholder_text="Enter student name...", width=250)
        self.entry.pack(side=LEFT)

        # Buttons
        buttons_frame = CTkFrame(self.master, fg_color="transparent")
        buttons_frame.pack(pady=10)

        self.create_button(buttons_frame, "Add", self.add_student, 0)
        self.create_button(buttons_frame, "Remove", self.remove_student, 1)
        self.create_button(buttons_frame, "Check", self.check_student, 2)
        self.create_button(buttons_frame, "Update", self.update_student, 3)
        self.create_button(buttons_frame, "Clear All", self.clear_students, 4)
        self.create_button(buttons_frame, "Exit", self.master.quit, 5)

        # Student List
        self.list_frame = CTkFrame(self.master)
        self.list_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

        self.scroll_frame = CTkScrollableFrame(self.list_frame)
        self.scroll_frame.pack(fill=BOTH, expand=True)
        self.student_labels = []

    def create_button(self, parent, text, command, col):
        btn = CTkButton(parent, text=text, command=command, width=120, height=35, corner_radius=10)
        btn.grid(row=0, column=col, padx=5, pady=5)

    def show_message(self, text, color="white"):
        self.message_var.set(text)
        self.message_label.configure(text_color=color)
        self.master.after(3000, lambda: self.message_var.set(""))

    def refresh_listbox(self):
        for widget in self.student_labels:
            widget.destroy()
        self.student_labels.clear()

        for student in sorted(self.students):
            lbl = CTkLabel(self.scroll_frame, text=student, font=("Arial", 16), anchor="w")
            lbl.pack(fill=X, padx=10, pady=2)
            self.student_labels.append(lbl)

    def add_student(self):
        name = self.entry_var.get().strip().title()
        if not name:
            self.show_message("Please enter a student name.", "orange")
            return
        if name in self.students:
            self.show_message(f"{name} already exists.", "red")
            return
        self.students.append(name)
        self.save_students()
        self.entry_var.set("")
        self.refresh_listbox()
        self.show_message(f"{name} added successfully!", "green")

    def remove_student(self):
        name = self.entry_var.get().strip().title()
        if not name:
            self.show_message("Enter student name to remove.", "orange")
            return
        if name not in self.students:
            self.show_message(f"{name} not in list.", "red")
            return
        self.students.remove(name)
        self.save_students()
        self.refresh_listbox()
        self.entry_var.set("")
        self.show_message(f"{name} removed.", "green")

    def check_student(self):
        name = self.entry_var.get().strip().title()
        if not name:
            self.show_message("Enter student name to check.", "orange")
            return
        if name in self.students:
            self.show_message(f"{name} is in the list.", "skyblue")
        else:
            self.show_message(f"{name} not found.", "red")

    def update_student(self):
        name = self.entry_var.get().strip().title()
        if not name:
            self.show_message("Enter a student name to update.", "orange")
            return
        if name not in self.students:
            self.show_message(f"{name} not found.", "red")
            return

        self.entry_var.set("")
        self.show_message(f"Type new name for '{name}' and press Enter", "skyblue")

        def apply_update(event):
            new_name = self.entry_var.get().strip().title()
            if not new_name:
                self.show_message("New name cannot be empty.", "orange")
                return
            if new_name in self.students:
                self.show_message("Name already exists.", "red")
                return
            index = self.students.index(name)
            self.students[index] = new_name
            self.save_students()
            self.refresh_listbox()
            self.show_message(f"Updated to {new_name}", "green")
            self.entry_var.set("")
            self.entry.unbind("<Return>")

        self.entry.bind("<Return>", apply_update)

    def clear_students(self):
        if not self.students:
            self.show_message("Student list is already empty.", "orange")
            return
        self.students.clear()
        self.save_students()
        self.refresh_listbox()
        self.show_message("All students cleared.", "green")

if __name__ == "__main__":
    root = CTk()
    app = App(root)
    root.mainloop()

