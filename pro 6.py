from datetime import datetime
import os

FILENAME = "journal.txt"

def display_menu():
    print("\nWelcome to Personal Journal Manager!")
    print("Please select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

def add_entry():
    entry_text = input("\nEnter your journal entry:\n")
    # Format the current timestamp precisely as [YYYY-MM-DD HH:MM:SS]
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    
    # Open file in append mode ('a') so it creates it if it doesn't exist
    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}\n{entry_text}\n\n")
        
    print("\nEntry added successfully!")

def view_entries():
    # If the file does not exist, display the error directly
    if not os.path.exists(FILENAME):
        print("\nOutput (If the file does not exist):")
        print("No journal entries found. Start by adding a new entry!")
        return

    print("\nOutput (If the file exists):")
    print("Your Journal Entries:")
    print("-" * 40)
    with open(FILENAME, "r", encoding="utf-8") as file:
        content = file.read().strip()
        if content:
            print(content)
        else:
            print("No journal entries found. Start by adding a new entry!")

def search_entry():
    keyword = input("\nEnter a keyword or date to search: ").lower()
    
    if not os.path.exists(FILENAME):
        print("\nOutput (If no match is found):")
        print(f"No entries were found for the keyword: {keyword}")
        return

    with open(FILENAME, "r", encoding="utf-8") as file:
        # Split by double newline to grab complete blocks (timestamp + text)
        content = file.read().strip()
        if not content:
            print("\nOutput (If no match is found):")
            print(f"No entries were found for the keyword: {keyword}")
            return
            
        entries = content.split("\n\n")
    
    matching_entries = []
    for entry in entries:
        if keyword in entry.lower():
            matching_entries.append(entry)
            
    if matching_entries:
        print("\nOutput (If a match is found):")
        print("Matching Entries:")
        print("-" * 40)
        print("\n\n".join(matching_entries))
    else:
        print("\nOutput (If no match is found):")
        print(f"No entries were found for the keyword: {keyword}")

def delete_entries():
    print("\nUser Input:\n4")
    confirm = input("\nAre you sure you want to delete all entries? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
            print("\nOutput (If the file is deleted successfully):")
            print("All journal entries have been deleted.")
        else:
            print("\nOutput (If the file does not exist):")
            print("No journal entries to delete.")
    else:
        print("Deletion canceled.")

def main():
    while True:
        display_menu()
        user_input = input("\nUser Input:\n").strip()
        
        if user_input == "1":
            add_entry()
        elif user_input == "2":
            # Extra safeguard for option 2 matching your specific "File Not Found Error" requirement image
            if not os.path.exists(FILENAME):
                print("\nOutput:")
                print("Error: The journal file does not exist. Please add a new entry first.")
            else:
                view_entries()
        elif user_input == "3":
            search_entry()
        elif user_input == "4":
            delete_entries()
        elif user_input == "5":
            print("\nOutput:")
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("\nOutput:")
            print("Invalid option. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()
