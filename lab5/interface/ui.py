import os
from models.enhanced_string import EnhancedString
from models.task_manager import TaskManager
from utils.task_logger import TaskLogger

class UserInterface:
    """Class to handle user interface for task management and string operations.
    
    This class provides a text-based interface for users to interact with the task
    management system and enhanced string operations.

    Attributes:
        task_manager (TaskManager): Handles core functionality of task management

    Menu Options:
        1. 📝 Create new task
        2. 👤 Assign task
        3. 📊 Update task status
        4. 📖 View task info
        5. 📋 List all tasks
        6. 🔤 String operations
        0. 🚪 Exit
    """
    def __init__(self, task_manager: TaskManager):
        self.task_manager = task_manager
        self.logger = TaskLogger()
        
    def show_menu(self):
        """Display the main menu interface."""
        menu_options = [
            "📝 1. Create new task",
            "👤 2. Assign task",
            "📊 3. Update task status",
            "📖 4. View task info",
            "📋 5. List all tasks",
            "🔤 6. String operations",
            "🚪 0. Exit"
        ]

        os.system('cls')
        print("\nLab 5 by Buliukin Volodimir | Group: KN-24 | Variant: 3")
        print("\n.・。.・゜✭・.・✫・゜・。.・゜✭・.・")
        for option in menu_options:
            print(f"  ✧ {option}")
        print(".・。.・゜✭・.・✫・゜・。.・゜✭・.・ ")
        self.handle_menu_choice()

    def display_tasks(self, tasks: dict) -> None:
        """
        Display all tasks in a formatted way.
        
        Args:
            tasks: Dictionary containing tasks to display
        """
        os.system('cls') 
        
        if not tasks:
            self.logger.print("No tasks found!", "info")
            input("\nPress Enter to return to menu...")
            self.show_menu()
            return
        
        self.logger.print("All Tasks:", "task_info")
        print("\n" + "─" * 50)
        
        for task_name, task_info in tasks.items():
            print(f"\nTask: {task_name}")
            print(f"  Description: {task_info['description']}")
            print(f"  Assignee: {task_info['assignee'] or 'Not assigned'}")
            print(f"  Status: {task_info['status']}")
            print("─" * 50)

    def handle_menu_choice(self, choice=None):
        """Process user's menu selection and execute corresponding operation."""
        try:
            if choice is None:
                choice = input(f"\n✨ Enter your choice (0-6): ")
            if choice == "0":
                self.logger.print("Exiting program...", "exit")
                exit()
            elif choice == "1":
                os.system('cls')

                self.logger.print("Create New Task", "task_created")
                name = input("Enter task name: ")
                desc = input("Enter task description: ")
            
                self.task_manager.create_task(name, desc)
                self.logger.print("Task created successfully!", "success")

                if self.ask_to_continue() == True:
                    self.handle_menu_choice("1")
                else: self.show_menu()
            elif choice == "2":
                os.system('cls')
                
                self.logger.print("Assign Task", "task_assigned")
                name = input("Enter task name: ")
                assignee = input("Enter assignee name: ")
                try:
                    self.task_manager.assign_task(name, assignee)
                    self.logger.print("Task assigned successfully!", "success")
                except ValueError as e:
                    self.logger.print(str(e), "error")
                
                if self.ask_to_continue():
                    self.handle_menu_choice()
                self.show_menu()
            elif choice == "3":
                os.system('cls')

                self.logger.print("Update Task Status", "status_update")
                name = input("Enter task name: ")
                status = input("Enter new status: ")
                
                try:
                    self.task_manager.update_status(name, status)
                    self.logger.print("Status updated successfully!", "success")
                except ValueError as e:
                    self.logger.print(str(e), "error")

                if self.ask_to_continue():
                    self.handle_menu_choice("3")
                self.show_menu()
            elif choice == "4":
                os.system('cls')
                
                self.logger.print("View Task Info", "task_info")
                name = input("Enter task name: ")
                try:
                    info = self.task_manager.get_task_info(name)
                    self.logger.print("\nTask Information:")
                    for key, value in info.items():
                        self.logger.print(f"  {key}: {value}")
                except ValueError as e:
                    self.logger.print(str(e), "error")
                
                if self.ask_to_continue():
                    self.handle_menu_choice("4")
                self.show_menu()

            elif choice == "5":
                os.system('cls')

                self.logger.print("List All Tasks", "task_info")
                self.display_tasks(self.task_manager.get_all_tasks())

                if self.ask_to_continue():
                    self.handle_menu_choice("5")
                self.show_menu()
            
            elif choice == "6":
                os.system('cls')
                
                self.logger.print("String Operations", "string_op")
                text = input("Enter text to analyze: ")
                enhanced = EnhancedString(text)
                
                self.logger.print("\nPalindrome Check:", "palindrome")
                result = "✅" if enhanced.is_palindrome() else "❌"
                self.logger.print(f"Result: {result}")
                
                seq = input("\nEnter sequence to check for repetition: ")
                self.logger.print("Sequence Check:", "sequence")
                has_repeating = enhanced.has_repeating_sequences(seq)
                result = "✅" if has_repeating else "❌"
                self.logger.print(f"Result: {result}")

                if self.ask_to_continue():
                    self.handle_menu_choice("6")
                self.show_menu()
            else:
                self.logger.print("Invalid choice! Please try again.", "error")
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

