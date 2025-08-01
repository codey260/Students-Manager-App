import customtkinter as ctk

class StudentApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Manager")
        self.master.geometry("400x600")

        self.student_names = []
        self.student_labels = []

        self.top_frame = ctk.CTkFrame(master)
        self.top_frame.pack(fill="x", padx=10, pady=(10, 0))

        self.middle_frame = ctk.CTkFrame(master)
        self.middle_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.bottom_frame = ctk.CTkFrame(master)
        self.bottom_frame.pack(fill="x", padx=10, pady=(0, 10))

        self.entry = ctk.CTkEntry(self.top_frame, placeholder_text="Enter student name")
        self.entry.pack(fill="x", padx=10, pady=10)

        self.status_label = ctk.CTkLabel(self.top_frame, text="", text_color="green")
        self.status_label.pack(pady=(0, 10))

        self.scroll_frame = ctk.CTkScrollableFrame(self.middle_frame)
        self.scroll_frame.pack(expand=True, fill="both")

        self.add_button = ctk.CTkButton(self.bottom_frame, text="Add", command=self.add_student)
        self.add_button.pack(side="left", expand=True, fill="x", padx=5)

        self.update_button = ctk.CTkButton(self.bottom_frame, text="Update", command=self.update_student)
        self.update_button.pack(side="left", expand=True, fill="x", padx=5)

        self.remove_button = ctk.CTkButton(self.bottom_frame, text="Remove", command=self.remove_student)
        self.remove_button.pack(side="left", expand=True, fill="x", padx=5)

        self.selected_index = None

        self.master.bind("<Configure>", self.on_resize)

    def add_student(self):
        name = self.entry.get().strip()
        if name:
            label = ctk.CTkLabel(self.scroll_frame, text=name)
            label.bind("<Button-1>", lambda e, i=len(self.student_labels): self.select_student(i))
            label.pack(fill="x", pady=2, padx=10)

            self.student_names.append(name)
            self.student_labels.append(label)

            self.entry.delete(0, 'end')
            self.status_label.configure(text="Student added", text_color="green")

    def select_student(self, index):
        if self.selected_index is not None:
            self.student_labels[self.selected_index].configure(fg_color="transparent")
        self.selected_index = index
        self.student_labels[index].configure(fg_color=("gray85", "gray25"))
        self.status_label.configure(text=f"Selected: {self.student_names[index]}", text_color="blue")

    def update_student(self):
        name = self.entry.get().strip()
        if self.selected_index is not None and name:
            self.student_names[self.selected_index] = name
            self.student_labels[self.selected_index].configure(text=name)
            self.entry.delete(0, 'end')
            self.status_label.configure(text="Student updated", text_color="orange")

    def remove_student(self):
        if self.selected_index is not None:
            self.student_labels[self.selected_index].destroy()
            del self.student_labels[self.selected_index]
            del self.student_names[self.selected_index]
            self.selected_index = None
            self.status_label.configure(text="Student removed", text_color="red")

    def on_resize(self, event):
        new_size = max(12, int(event.width / 25))
        for lbl in self.student_labels:
            lbl.configure(font=("Arial", new_size))

if __name__ == '__main__':
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    app = StudentApp(root)
    root.mainloop()

