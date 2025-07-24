# 🎓 Students Manager

**Students Manager** is a simple educational project built with **Python**.  
Its main purpose is to **manage a student group** with a clean graphical user interface (GUI) using `tkinter`.  
This project demonstrates basic CRUD operations for managing students and shows how to integrate traditional Python logic with a GUI.

---

## 📌 Project Description

- **Name:** Students Manager
- **Type:** Python GUI Application
- **Purpose:** Add, remove, check, display, and clear students easily through an intuitive GUI.
- **Original Logic:** Created by `youcefshaaban`.
- **GUI Integration:** Implemented with `tkinter` and smart in-memory storage.

---

## ⚙️ Available Functions

| Function           | Description                                               |
| ------------------ | --------------------------------------------------------- |
| `add_student()`    | Add a new student to the list                             |
| `remove_student()` | Remove a selected student from the list                   |
| `check_student()`  | Check if a student exists in the list                     |
| `show_students()`  | Display all students (managed via the listbox in the GUI) |
| `clear_students()` | Clear all students from the list with confirmation        |
| `update_student()` | Update an existing student to a new name                  |

---

## 💾 Data Persistence

**How does it store the data?**

- This project uses **In-Memory Serialization** (`pickle`) to store the list of students **inside the program memory only**.
- The data **will persist as long as the program is running**.
- **Note:** Once you close and re-open the app, the student list resets because no external files or databases are used.

This approach is perfect for simple demos and educational use.

---

## ✅ Requirements

To run this project, you need:

- **Python 3.7+**
- Standard Python library only:
  - `tkinter` (usually bundled with Python)
  - `pickle` (built-in)

No third-party packages required.

---

## 🖥️ Supported Operating Systems

This project runs on:

- ✅ **Windows** (tested)
- ✅ **Linux** (tested)
- ✅ **macOS** (should work as long as `tkinter` is installed)

---

## 🚀 How to Run

```bash
# 1️⃣ Make sure you have Python installed:
python --version

# 2️⃣ Run the Python file:
python app.py
```
### Then you are ready to go.
