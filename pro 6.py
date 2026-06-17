from datetime import datetime import os
filename ="journal.txt"
def display_menu():
    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option")
        print("1. Add a new entry")
        print("2. View all entries")
        print("3. Search for an entry")
        print("4. Delete all entries")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            entry = input("Enter your journal entry: ")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(file_name, "a") as file:
                file.write(f"[{timestamp}] {entry}\n")

            print("Entry added successfully!")

        elif choice == 2:
            try:
                with open(file_name, "r") as file:
                    content = file.read()

                if content:
                    print("\n--- Journal Entries ---")
                    print(content)
                else:
                    print("No entries found.")

            except FileNotFoundError:
                print("No journal entries found.")

        elif choice == 3:
            keyword = input("Enter keyword to search: ")

            try:
            with open(file_name, "r") as file:
                 found = False

                 for line in file:
            if keyword.lower() in line.lower():
                    print(line.strip())
                     found = True

            if not found:
                 print("No matching entries found.")

                except FileNotFoundError:
                 print("No journal file found.")

           elif choice == 4:
                confirm = input(
                "Are you sure you want to delete all entries? (yes/no): ")
               

         if confirm.lower() == "yes":
            open(file_name, "w").close()
            print("All entries deleted.")
         else:
           print("Deletion cancelled.")

         elif choice == 5:
              print("Goodbye!")
              break

        else:
            print("Invalid choice. Please select 1-5.")

# Run the program

