import os
from typing import List
from utils.logger import Logger

class FileManager:
    """Class to manage file operations for student groups."""
    def __init__(self, directory: str, logger: Logger):
        self.directory = directory
        self.log = logger
        self._ensure_directory_exists()

    def _ensure_directory_exists(self):
        """Ensure the directory exists, create it if not."""

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
            self.log.print("Created new directory", "setup")
        else:
            self.log.print("Directory already exists", "exists")

    def create_group_file(self, group_name: str):
        """Create a new group file with the specified group name."""

        self.log.print(f"Creating group file for '{group_name}'...", "folder")
        group_path = os.path.join(self.directory, f"{group_name}.txt")

        if not os.path.exists(group_path):
            with open(group_path, 'w') as file:
                file.write(f"Students\nGroup: {group_name}\n\n")
            self.log.print(f"Group file '{group_name}.txt' created successfully.", "succ")
        else:
            self.log.print(f"Group file '{group_name}.txt' already exists.", "exists")

    def group_exists(self, group_name: str) -> bool:
        """Check if a group exists."""
        group_path = os.path.join(self.directory, f"{group_name}.txt")
        exists = os.path.exists(group_path)
        if not exists:
            self.log.print(f"Group {group_name} does not exist", "err")
        return exists
    
    def has_duplicate_name(self, group_name: str, student_name: str) -> bool:
        """Check if a student name already exists in the group file."""
        group_path = os.path.join(self.directory, f"{group_name}.txt")
        
        if not os.path.exists(group_path):
            return False
            
        try:
            with open(group_path, 'r') as file:
                for line in file:
                    if line.strip() and line[0].isdigit():
                        # Split the line to get the student name
                        existing_name = line.split('.')[1].split('\t')[0].strip()
                        if existing_name.lower() == student_name.lower():
                            return True
            return False
        except Exception as e:
            self.log.print(f"Error checking for duplicates: {str(e)}", "err")
            return False
        
    def show_group_file(self, group_name: str) -> bool:
        """Display contents of a group file."""
        if not self.group_exists(group_name):
            return False
            
        self.log.print(f"Reading group file '{group_name}'...", "search")
        group_path = os.path.join(self.directory, f"{group_name}.txt")
            
        try:
            with open(group_path, 'r') as file:
                print("\nFile contents:")
                print("-" * 40)
                print(file.read().strip())
                print("-" * 40 + "\n")
            return True
        except Exception as e:
            self.log.print(f"Error reading file: {str(e)}", "err")
            return False

    def sort_by_gpa(self, group_name: str):
        """Сортировка студентов по среднему баллу."""
        group_path = os.path.join(self.directory, f"{group_name}.txt")
        
        if not os.path.exists(group_path):
            self.log.print(f"Group {group_name} does not exist", "err")
            return False
            
        try:
            with open(group_path, 'r') as file:
                lines = file.readlines()

            header = []
            students = []
            for line in lines:
                if line.strip() and line[0].isdigit():
                    try:
                        # Split line: "1. \t |85.5 \t | John Smith"
                        id_part = line.split('.')[0].strip()  # "1"
                        rest = line.split('|')  # [" 1. \t ", "85.5 \t ", " John Smith\n"]
                        
                        if len(rest) >= 2:
                            gpa_str = rest[1].strip()  # "85.5"
                            name = rest[2].strip()  # "John Smith"
                            
                            try:
                                gpa = float(gpa_str)
                                students.append((int(id_part), name, gpa))
                            except ValueError:
                                self.log.print(f"Uncorrect Value GPA in line: {line.strip()}", "warn")
                    except IndexError:
                        self.log.print(f"Uncorrect line format: {line.strip()}", "warn")
                else:
                    header.append(line)
            
            if not students:
                self.log.print("No student records found for sorting", "warn")
                return False
                
            # Sort students by GPA in descending order
            students.sort(key=lambda x: x[2], reverse=True)
            
            with open(group_path, 'w') as file: # Write sorted data back to file
                file.writelines(header)
                for index, (_, name, gpa) in enumerate(students, 1):
                    file.write(f"{index}. \t |{gpa:.1f} \t | {name}\n")
            
            self.log.print(f"Group file '{group_name}' sorted by GPA", "succ")
            return True
            
        except Exception as e:
            self.log.print(f"Error sorting by GPA: {str(e)}", "err")
            return False