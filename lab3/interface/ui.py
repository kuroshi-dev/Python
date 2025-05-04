import os
from managers.student_manager import StudentManager

class UserInterface:
    """Class to handle user interface interactions for the student management system."""
    def __init__(self, student_manager: StudentManager):
        self.student_manager = student_manager

    def show_menu(self):
        """Display the main menu and handle user input."""
        self.student_manager.log.print("Main Menu", "setup")
        menu_options = [
            "📖 1. Read student data from group",
            "✏️  2. Add student to group",
            "❌ 3. Delete student from group",
            "📁 4. Search files",
            "🔍 5. Search student in group",
            "📊 6. Sort students by GPA",
            "🚪 0. Exit"
        ]

        os.system('cls')
        print("\nLab 3 by Buliukin Volodimir | Group: KN-24 | Variant: 3")
        print("\n.・。.・゜✭・.・✫・゜・。.・゜✭・.・")
        for option in menu_options:
            print(f"  ✧ {option}")
        print(".・。.・゜✭・.・✫・゜・。.・゜✭・.・ ")
        self.handle_menu_choice()

    def handle_menu_choice(self, choice=None):
        try:
            if choice is None:
                choice = input(f"\n✨ Enter your choice (0-6): ")
            if choice == "0":
                self.student_manager.log.print("Exiting program...", "exit")
                exit()
            elif choice == "1":
                os.system('cls')
                group = input("Enter group number: ")
                
                self.student_manager.file_manager.show_group_file(group)

                if self.ask_to_continue() == True:
                    self.handle_menu_choice("1")
                else: self.show_menu()
            elif choice == "2":
                os.system('cls')
                
                group = input("Enter group number: ")
                self.student_manager.file_manager.show_group_file(group)
                name = input("Enter student name: ")
                gpa = float(input("Enter student GPA: "))

                self.student_manager.add_student(group, name, gpa)
                if self.ask_to_continue():
                    self.handle_menu_choice()
                self.show_menu()
            elif choice == "3":
                os.system('cls')

                group = input("Enter group number: ")
                self.student_manager.file_manager.show_group_file(group)
                self.student_manager.log.print("Enter student ID or name to delete:", "search")
                name = input("")
                self.student_manager.delete_student(group, name)
                if self.ask_to_continue():
                    self.handle_menu_choice("3")
                self.show_menu()
            elif choice == "4":
                os.system('cls')
                pattern = input("Enter search pattern (or press Enter for all files): ")
                files = self.student_manager.file_manager.search_files(pattern)
                if files:
                    print("\nFound files:")
                    for file in files:
                        print(f"📄 {file}")
                else:
                    self.student_manager.log.print("No files found", "warn")
                
                if self.ask_to_continue():
                    self.handle_menu_choice("4")
                self.show_menu()

            elif choice == "5":
                os.system('cls')
                group = input("Enter group number: ")
                search_term = input("Enter search term: ")
                results = self.student_manager.file_manager.search_in_file(group, search_term)
                
                if results:
                    print("\nSearch results:")
                    for result in results:
                        print(f"➜ {result}")
                else:
                    self.student_manager.log.print("No matches found", "warn")
                
                if self.ask_to_continue():
                    self.handle_menu_choice("5")
                self.show_menu()

            elif choice == "6":
                os.system('cls')
                group = input("Enter group number: ")
                if self.student_manager.file_manager.sort_by_gpa(group):
                    self.student_manager.file_manager.show_group_file(group)
                
                if self.ask_to_continue():
                    self.handle_menu_choice("6")
                self.show_menu()
            else:
                self.student_manager.log.print("Invalid choice! Please try again.", "warning")
                self.show_menu()

        except ValueError as e:
            self.student_manager.log.print(f"Invalid input: {str(e)}", "err")
            self.show_menu()

    @staticmethod
    def ask_to_continue() -> bool:
        print("🔄 " + "Do you want to call this function again? (y/n): ")
        again = input().strip().lower()
        return again == "y"
        
