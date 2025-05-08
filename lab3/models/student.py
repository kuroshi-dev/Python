from typing import Tuple

class Student:
    """
    Class representing a student.
    
    A class representing a student with a name and Grade Point Average (GPA).
    This class stores and manages student information including their full name
    and academic performance measured by GPA.
    Attributes:
        name (str): The full name of the student. Must contain only letters and spaces.
        gpa (float): The Grade Point Average of the student. Must be between 0.0 and 100.0.
    Methods:
        validate_student_data(name: str, gpa: float) -> Tuple[bool, str]:
            Static method that validates the student data before creation.
            Returns a tuple containing validation status and error message if any.
    Examples:
        >>> student = Student("John Smith", 85.5)
        >>> student.name
        'John Smith'
        >>> student.gpa
        85.5
        >>> Student.validate_student_data("John Smith", 95.5)
        (True, '')
        >>> Student.validate_student_data("John123", 85.5)
        (False, 'Student name should contain only letters and spaces')
    """
    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa

    @staticmethod # static method to validate student data
    def validate_student_data(name: str, gpa: float) -> Tuple[bool, str]:
        if not all(c.isalpha() or c.isspace() for c in name):
            return False, "Student name should contain only letters and spaces"
        try:
            gpa = float(gpa)
            if not (0.0 <= gpa <= 100.0):
                return False, "GPA must be between 0.0 and 100.0"
        except ValueError:
            return False, "GPA must be a valid number"
        return True, ""