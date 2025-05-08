import os
from typing import List
from utils.logger import Logger

class FileManager:
    """Class to manage file operations for student groups.

    This class provides functionality to manage student group files, including creation,
    reading, and manipulation of group data files in a specified directory.

    ----------------------------------------

    Args:
        directory (str): The base directory path where group files are stored.
        log (Logger): Logger instance for recording operations and errors.

    Methods:
        _ensure_directory_exists(): `Creates the directory if it doesn't exist.`
        create_group_file(group_name: str): `Creates a new file for a student group.`
        group_exists(group_name: str) -> bool: `Checks if a group file exists.`
        has_duplicate_name(group_name: str, student_name: str) -> bool: `Checks for duplicate student names in a group.`
        show_group_file(group_name: str) -> bool: `Displays the contents of a group file.`
        sort_by_gpa(group_name: str) -> bool: `Sorts students in a group by their GPA.`

    Note:
        File Format:
            Each group file is a text file with the following structure:
            - Header with group information
            - Student entries in format: "index. | gpa | name"

    Examples:
        >>> file_manager = FileManager("./groups", logger)
        >>> file_manager.create_group_file("121")
        >>> file_manager.show_group_file("121")
        >>> file_manager.sort_by_gpa("121")

    Raises:
        OSError: If there are issues with file/directory operations
        Exception: For general errors during file operations
    """
    def __init__(self, directory: str, logger: Logger):
        self.directory = directory
        self.log = logger
        self._ensure_directory_exists()

    def _ensure_directory_exists(self):
        """
        Ensures that the specified directory exists, creating it if necessary.

        This method checks if the directory specified in self.directory exists.
        If not, it creates the directory and logs the creation.

        ----------------------------------------

        Side Effects:
            - Creates a new directory if it doesn't exist
            - Logs messages about directory status

        Returns:
            None
        """

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
            self.log.print("Created new directory", "setup")
        else:
            self.log.print("Directory already exists", "exists")

    def create_group_file(self, group_name: str):
        """
        Creates a new file for a student group.

        This method creates a new text file for storing student group data
        with a specified group name.

        ----------------------------------------

        Args:
            group_name (str): The name of the group to create

        Side Effects:
            - Creates a new text file if it doesn't exist
            - Logs messages about file creation status

        Returns:
            None
        """

        self.log.print(f"Creating group file for '{group_name}'...", "folder")

    def search_files(self, pattern: str) -> List[str]:
        """
        Searches for files in the directory matching a specified pattern.

        This method searches through the directory for files that match the
        given pattern and returns a list of matching file names.

        ----------------------------------------

        Args:
            pattern (str): The search pattern to match file names

        Returns:
            List[str]: A list of matching file names
        """

        self.log.print(f"Searching for files with pattern '{pattern}'...", "search")
        files = [f for f in os.listdir(self.directory) if pattern in f]
        self.log.print(f"Found {len(files)} files matching '{pattern}'", "succ")
        return files

    def group_exists(self, group_name: str) -> bool:
        """
        Checks if a group file exists.

        Verifies whether a file for the specified group exists in the directory.

        ----------------------------------------

        Args:
            group_name (str): The name of the group to check

        Returns:
            bool: True if the group file exists, False otherwise
        """
        group_path = os.path.join(self.directory, f"{group_name}.txt")
        exists = os.path.exists(group_path)
        if not exists:
            self.log.print(f"Group {group_name} does not exist", "err")
        return exists
    
    def has_duplicate_name(self, group_name: str, student_name: str) -> bool:
        """
        Checks for duplicate student names in a group.

        Searches through the specified group file for any matching student names.

        ----------------------------------------

        Args:
            group_name (str): The name of the group to check
            student_name (str): The student name to look for

        Returns:
            bool: True if the name exists in the group, False otherwise

        Raises:
            Exception: If there are errors reading the file
        """
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
        
    def search_in_file(self, group_name: str, pattern: str) -> List[str]:
        """
        Searches for a pattern in a group file.

        This method searches through the specified group file for lines
        containing the given pattern.

        ----------------------------------------

        Args:
            group_name (str): The name of the group to search
            pattern (str): The search pattern

        Returns:
            List[str]: A list of matching lines from the file
        """
        group_path = os.path.join(self.directory, f"{group_name}.txt")
        
        if not os.path.exists(group_path):
            return []
            
        try:
            with open(group_path, 'r') as file:
                lines = [line.strip() for line in file if pattern.lower() in line.lower()]
            return lines
        except Exception as e:
            self.log.print(f"Error searching in file: {str(e)}", "err")
            return []
        
    def show_group_file(self, group_name: str) -> bool:
        """
        Displays the contents of a group file.

        Reads and prints the contents of the specified group file.

        ----------------------------------------

        Args:
            group_name (str): The name of the group to display

        Returns:
            bool: True if file was successfully displayed, False otherwise

        Side Effects:
            - Prints file contents to console
            - Logs operation status
        """
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

    def sort_by_gpa(self, group_name: str) -> bool:
        """
        Sorts students in a group by their GPA.

        Reads the group file, sorts students by GPA in descending order,
        and writes the sorted data back to the file.

        ----------------------------------------

        Args:
            group_name (str): The name of the group to sort

        Returns:
            bool: True if sorting was successful, False otherwise

        Side Effects:
            - Modifies the group file content
            - Updates student IDs according to new order
            - Logs operation status

        Note:
            Format of student entries: "index. | gpa | name"

        Examples:
            >>> file_manager = FileManager("groups", logger)
            >>> file_manager.sort_by_gpa("121")
            True
            >>> # File contents before:
            >>> # 1. |85.5 | John Smith
            >>> # 2. |90.0 | Emma Davis
            >>> # File contents after:
            >>> # 1. |90.0 | Emma Davis
            >>> # 2. |85.5 | John Smith
        """
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
                for index, (_, name, gpa) in enumerate(students, 1): # Start index from 1
                    file.write(f"{index}. \t |{gpa:.1f} \t | {name}\n") # Format GPA to one decimal place
            
            self.log.print(f"Group file '{group_name}' sorted by GPA", "succ")
            return True
            
        except Exception as e:
            self.log.print(f"Error sorting by GPA: {str(e)}", "err")
            return False