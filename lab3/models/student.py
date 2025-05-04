from typing import Tuple

class Student:
    """Class representing a student with a name and GPA."""
    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa

    @staticmethod
    def validate_student_data(name: str, gpa: float) -> Tuple[bool, str]:
        if not all(c.isalpha() or c.isspace() for c in name):
            return False, "Student name should contain only letters and spaces"
        try:
            gpa = float(gpa)
            if not 0.0 <= gpa <= 100.0:
                return False, "GPA must be between 0.0 and 100.0"
        except ValueError:
            return False, "GPA must be a valid number"
        return True, 