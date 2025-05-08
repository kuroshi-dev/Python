import os
from managers.student_manager import StudentManager

class UserInterface:
    """Class to handle user interface for student management system.
    
    This class provides a text-based interface for users to interact with the student
    management system, offering various operations for managing student data.

    ----------------------------------------

    Attributes:
        student_manager (StudentManager): Handles core functionality of student management

    Methods:
        show_menu(): Displays main menu and handles navigation
        handle_menu_choice(choice): Processes user input and executes operations
        ask_to_continue(): Prompts for operation repetition

    Menu Options:
        1. 📖 Read student data from group
        2. ✏️ Add student to group
        3. ❌ Delete student from group
        4. 📁 Search files
        5. 🔍 Search student in group
        6. 📊 Sort students by GPA
        0. 🚪 Exit

    Examples:
        >>> ui = UserInterface(student_manager)
        >>> ui.show_menu()

    Note:
        Uses emoji icons and Unicode characters for better visual representation
    """
    def __init__(self, student_manager: StudentManager):
        self.student_manager = student_manager

    def show_menu(self):
        """Display the main menu interface.

        This method presents a graphical menu interface with various options
        for managing student data.

        ----------------------------------------

        Side Effects:
            - Clears console screen
            - Prints menu options
            - Handles user input

        Note:
            Uses Unicode characters for decorative borders and emoji icons

        Examples:
            >>> ui = UserInterface(student_manager)
            >>> ui.show_menu()
            🔧 Main Menu
            
            Lab 3 by Buliukin Volodimir | Group: KN-24 | Variant: 3
            .・。.・゜✭・.・✫・゜・。.・゜✭・.・
              ✧ 📖 1. Read student data from group
              ✧ ✏️ 2. Add student to group
              ... other menu options...
            .・。.・゜✭・.・✫・゜・。.・゜✭・.・
        """
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
        """Process user's menu selection and execute corresponding operation.

        This method handles the logic for each menu option, including input
        validation and error handling.

        ----------------------------------------

        Args:
            choice (str, optional): Menu option number. Defaults to None.
                                  Valid choices are "0" through "6".

        Side Effects:
            - Executes selected operation
            - Handles navigation between menus
            - Shows error messages for invalid inputs

        Raises:
            ValueError: If input values are invalid
        """
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

    @staticmethod # Static method to ask user if they want to continue
    def ask_to_continue() -> bool:
        """Prompt user to repeat current operation.

        This method asks if the user wants to perform the same operation again.

        ----------------------------------------

        Returns:
            bool: True if user wants to continue, False otherwise

        Side Effects:
            - Prints prompt message
            - Waits for user input
        """
        print("🔄 " + "Do you want to call this function again? (y/n): ")
        again = input().strip().lower()
        return again == "y"

