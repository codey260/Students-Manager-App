# 🎓 Students Manager

**Students Manager** is a simple educational project built with **Python**.  
Its main purpose is to **manage a student group** with a clean graphical user interface (GUI) using `tkinter`.  
This project demonstrates basic CRUD operations for managing students and shows how to integrate traditional Python logic with a GUI.

---

## 📌 Project Description

- **Name:** Students Manager
- **Type:** Python GUI Application
- **Purpose:** Add, remove, check, display, and clear students easily through an intuitive GUI.
- **GUI Integration:** Implemented with `tkinter` and smart data persistence

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

- This project uses **Smart Data Serialization** (`json`) to store the list of students **in a json file**.
- The data **will persist as long as the data.json file is found**.
---

## ✅ Requirements

To run this project, you need:

- **Python 3.7+**
- Standard Python library only:
  - `tkinter` (usually bundled with Python)
  - `json` (built-in)

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
python3 --version

# 2️⃣ Run the Python file:
python3 app.py
```
### Then you are ready to go.
