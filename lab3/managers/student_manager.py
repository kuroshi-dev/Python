import os
import time
from utils.logger import Logger
from utils.file_manager import FileManager
from models.student import Student

class StudentManager:
    """Class to manage student groups and their data.

    This class provides functionality to manage student groups, including creating group files,
    adding students, and deleting students. It handles file operations and logging.

    ----------------------------------------

    Attributes:
        log (Logger): Logger instance for recording operations and errors
        file_manager (FileManager): Manages file operations for student groups

    Methods:
        _setup_logging(): Initializes logging and verifies working directory permissions
        create_group_file(*group_names): Creates new group files for given group names
        add_student(group_name, student_name, gpa): Adds a student to specified group
        delete_student(group_name, identifier): Removes a student from group

    Examples:
        >>> manager = StudentManager("groups")
        >>> manager.create_group_file("Group1", "Group2")
        >>> manager.add_student("Group1", "John Doe", 85.5)
        >>> manager.delete_student("Group1", "1")  # Delete by ID

    Note:
        - Group files are stored as .txt files in the specified directory
        - Student entries include ID, GPA and name
        - Duplicate student names are not allowed within the same group
    """
    def __init__(self, directory: str = "groups"):
        self.log = Logger()
        self.file_manager = FileManager(directory, self.log)
        self._setup_logging()

    def _setup_logging(self):
        """Initialize and configure logging for the Student Manager.

        This method sets up the initial logging configuration and performs 
        system checks for proper operation.

        ----------------------------------------

        Side Effects:
            - Announces initialization
            - Verifies working directory path
            - Checks directory permissions
            - Counts existing group files
            - Adds delays between operations

        Note:
            Each log message has a 0.5 second delay for better readability
        """
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
            
        # count for existing files
        existing_files = len([f for f in os.listdir(self.file_manager.directory) if f.endswith('.txt')])
        self.log.print(f"Found {existing_files} existing group file(s)", "exists")
        time.sleep(0.5)
        self.log.print("Setup complete", "succ")

    def create_group_file(self, *group_names: str):
        """Create group files for the specified group names.

        This method creates separate files for each specified group name
        using the file manager.

        ----------------------------------------

        Args:
            *group_names (str): Variable number of group names to create files for

        Side Effects:
            - Creates new text files in the groups directory
            - Logs creation status for each file

        Raises:
            IOError: If there are issues creating files
            ValueError: If any group name is invalid
        """
        self.log.print("Creating group files...", "folder")
        for group_name in group_names:
            self.file_manager.create_group_file(group_name)

    def add_student(self, group_name: str, student_name: str, gpa: float = 0.0):
        """Add a student to the specified group.

        This method adds a new student entry to the specified group file with
        an automatically assigned ID.

        ----------------------------------------

        Args:
            group_name (str): The group to add the student to
            student_name (str): The name of the student
            gpa (float, optional): Student's GPA. Defaults to 0.0

        Side Effects:
            - Modifies group file content
            - Logs operation status
            - Validates student data

        Note:
            Student format in file: "ID. | GPA | Name"

        Examples:
            >>> manager = StudentManager()
            >>> manager.add_student("121", "John Smith", 85.5)
            ✅ Added student 'John Smith' to group 121
            >>> manager.add_student("121", "John Smith", 90.0)
            ⚠️ Student with name 'John Smith' already exists in group 121
            >>> manager.add_student("999", "Emma Davis", 95.0)
            ❌ Error: Group 999 does not exist
        """
        if not self.file_manager.group_exists(group_name):
            return
        
        if self.file_manager.has_duplicate_name(group_name, student_name):
            self.log.print(f"Student with name '{student_name}' already exists in group {group_name}", "warn")
            return
        
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
        """Delete a student from the specified group.

        This method removes a student entry from the group file based on
        their ID or name.

        ----------------------------------------

        Args:
            group_name (str): The group to delete from
            student_identifier (str): Student's ID or name

        Side Effects:
            - Modifies group file content
            - Logs operation status

        Note:
            - Can delete by ID (e.g., "1") or name
            - Case-sensitive name matching
        """
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
