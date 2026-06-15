# 📔 Personal Journal Manager

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![File Handling](https://img.shields.io/badge/File_Handling-TXT-green?style=for-the-badge&logo=files&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-purple?style=for-the-badge&logo=windowsterminal&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> ✨ **A simple yet powerful command-line journal app built with Python** — write, read, search, and manage your daily thoughts, all saved locally!

</div>

---

## 🌟 Features

| 🔧 Feature | 📝 Description |
|-----------|---------------|
| ✍️ **Add Entry** | Write a new journal entry with automatic timestamp |
| 📖 **View All** | Read all your past journal entries at once |
| 🔍 **Search** | Find entries by keyword (case-insensitive) |
| 🗑️ **Delete All** | Clear all entries with a safety confirmation prompt |
| 🚪 **Exit** | Cleanly exit the program |

---

## 📸 Screenshots

### 🟢 Adding & Viewing Entries

![Screenshot 1 – Add and View](screenshot1.jpg)

> *Adding a new journal entry and viewing it back instantly with timestamp.*

---

### 🔵 Viewing & Searching Entries

![Screenshot 2 – View and Search](screenshot2.jpg)

> *Viewing all entries, then searching by keyword `productive` — results show instantly!*

---

### 🔴 Deleting Entries & Exiting

![Screenshot 3 – Delete and Exit](screenshot3.jpg)

> *Deleting all entries with a confirmation step, then exiting gracefully.*

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python **3.x** installed on your system
- No external libraries needed — uses Python's built-in `datetime` module only!

### ▶️ Run the Program

```bash
python pro_6.py
```

---

## 🎮 How to Use

Once you run the program, you'll see this menu:

```
Welcome to Personal Journal Manager!
Please select an option
1. Add a new entry
2. View all entries
3. Search for an entry
4. Delete all entries
5. Exit
```

### 📌 Option Guide

```
1️⃣  Add Entry   → Type your thoughts, saved with date & time
2️⃣  View All    → Displays all saved journal entries
3️⃣  Search      → Enter a keyword to find matching entries
4️⃣  Delete All  → Wipes the journal (asks for confirmation!)
5️⃣  Exit        → Safely closes the program
```

---

## 📁 Project Structure

```
📦 Personal Journal Manager
 ┣ 📄 pro_6.py        ← Main Python script
 ┣ 📄 journal.txt     ← Auto-created when first entry is added
 ┗ 📄 README.md       ← You're reading this!
```

---

## 🧠 How It Works

```python
# Each entry is saved like this inside journal.txt:
[2026-06-15 18:35:27] Today was a productive day. I learned about file handling in Python.
```

- 📅 **Timestamp** is auto-generated using Python's `datetime.now()`
- 💾 **Entries** are appended to `journal.txt` using file mode `"a"`
- 🔍 **Search** reads line-by-line and checks for case-insensitive keyword match
- 🗑️ **Delete** opens the file in write mode `"w"` to clear all content

---

## 💡 Concepts Used

- 🐍 Python Functions
- 📂 File Handling (`open`, `read`, `write`, `append`)
- 🕐 `datetime` module for timestamps
- 🔄 `while` loop for the interactive menu
- ⚠️ `try/except` for error handling (invalid input & missing file)

---

## 👨‍💻 Author

> Built with ❤️ using Python  
> Perfect for beginners learning **file I/O and CLI applications**!

---

<div align="center">

⭐ **If you found this helpful, give it a star!** ⭐

</div>
