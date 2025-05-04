import os
import time
from utils.logger import Logger
from utils.file_manager import FileManager
from models.student import Student

class StudentManager:
    """Class to manage student groups and their data."""
    def __init__(self, directory: str = "groups"):
        self.log = Logger()
        self.file_manager = FileManager(directory, self.log)
        self._setup_logging()

    def _setup_logging(self):
        """Initialize and log program setup."""
        self.log.print("Initializing Student Manager", "setup")
        time.sleep(0.5)
        self.log.print(f"Working directory: {os.path.abspath(self.file_manager.directory)}", "folder")
        time.sleep(0.5)
        
        # Check write permissions
        if os.access(self.file_manager.directory, os.W_OK):
            self.log.print("Write permissions verified", "check")
        else:
            self.log.print("No write permissions in directory", "warn")
        time.sleep(0.5)
            
        # Check for existing files
        existing_files = len([f for f in os.listdir(self.file_manager.directory) if f.endswith('.txt')])
        self.log.print(f"Found {existing_files} existing group file(s)", "exists")
        time.sleep(0.5)
        self.log.print("Setup complete", "succ")

    def create_group_file(self, *group_names: str):
        """Create group files for the specified group names."""
        self.log.print("Creating group files...", "folder")
        for group_name in group_names:
            self.file_manager.create_group_file(group_name)

    def add_student(self, group_name: str, student_name: str, gpa: float = 0.0):
        """Add a student to the specified group."""
        if not self.file_manager.group_exists(group_name):
            return
        
        if self.file_manager.has_duplicate_name(group_name, student_name):
            self.log.print(f"Student with name '{student_name}' already exists in group {group_name}", "warn")
            return
        
        self.log.print(f"Adding student '{student_name}' with GPA {gpa} to group '{group_name}'...", "edit")
        valid, message = Student.validate_student_data(student_name, gpa)
        if not valid:
            self.log.print(message, "err")
            return

        student_id = 1
        try:
            group_path = os.path.join(self.file_manager.directory, f"{group_name}.txt")
            with open(group_path, 'r') as file:
                for line in file:
                    if line.strip() and line[0].isdigit():
                        current_id = int(line.split('.')[0])
                        student_id = max(student_id, current_id + 1)

            with open(group_path, 'a') as file:
                file.write(f"{student_id}. \t |{gpa} \t | {student_name}\n")
            self.log.print(f"Added student '{student_name}' to group {group_name}", "succ")
        except Exception as e:
            self.log.print(f"Error adding student: {str(e)}", "err")

    def delete_student(self, group_name: str, student_identifier: str):
        """Delete a student from the specified group by name or ID."""
        if not self.file_manager.group_exists(group_name):
            return
            
        try:
            group_path = os.path.join(self.file_manager.directory, f"{group_name}.txt")
            with open(group_path, 'r') as file:
                lines = file.readlines()

            found = False
            new_lines = []
            for line in lines:
                if not line.strip():
                    new_lines.append(line)
                    continue
                
                if not line[0].isdigit():
                    new_lines.append(line)
                    continue
                    
                # Check if line matches either ID or name
                student_id = line.split('.')[0].strip()
                student_entry = line.split('.', 1)[1].strip()
                
                if student_identifier == student_id or student_identifier in student_entry:
                    found = True
                    continue
                new_lines.append(line)

            if not found:
                self.log.print(f"Student with identifier '{student_identifier}' not found in group {group_name}", "err")
                return
           
            with open(group_path, 'w') as file:
                file.writelines(new_lines)

            self.log.print(f"Deleted student with identifier '{student_identifier}' from group {group_name}", "succ")
            
        except Exception as e:
            self.log.print(f"Error deleting student: {str(e)}", "err")
