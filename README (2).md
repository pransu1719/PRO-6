# Personal Journal Manager

A simple command-line journal application written in Python. It lets you add, view, search, and delete journal entries, with each entry automatically timestamped.

## Features

- **Add a New Entry** — Write a journal entry and have it saved with a timestamp in the format `[YYYY-MM-DD HH:MM:SS]`.
- **View All Entries** — Display every saved entry in the order they were written.
- **Search for an Entry** — Search entries by keyword or date.
- **Delete All Entries** — Clear the journal file after a confirmation prompt.
- **Exit** — Quit the application.

All entries are stored locally in a plain text file (`journal.txt`), created automatically the first time you add an entry.

## How It Works

When you run the script, you're shown a menu:

```
Welcome to Personal Journal Manager!
Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

Simply enter the number corresponding to the action you want to perform.

## File

- [`journal_manager.py`](journal_manager.py) — the main script

## Screenshots

**Adding a new entry**

![Add entry](screenshots/191.png)

**Viewing all entries**

![View entries](screenshots/192.png)

**Deleting all entries (with confirmation)**

![Delete entries](screenshots/193.png)

**Viewing entries when no journal file exists**

![No file error](screenshots/194.png)

**Handling an invalid menu option and exiting**

![Invalid option and exit](screenshots/195.png)

## Requirements

- Python 3.x (no external libraries required — uses only `datetime` and `os` from the standard library)

## Usage

```bash
python journal_manager.py
```

Follow the on-screen menu prompts to manage your journal entries.
