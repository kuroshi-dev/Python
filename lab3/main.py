from managers.student_manager import StudentManager
from interface.ui import UserInterface
import random
    
def main():
    """Main function to run the program."""
    manager = StudentManager()
    manager.create_group_file("121", "122", "123")
    ui = UserInterface(manager)
    add = manager.add_student
    
    students = [
        ("121", "John Smith", str(random.randint(1, 100))),
        ("122", "Emma Davis", str(random.randint(1, 100))),
        ("123", "Michael Wilson", str(random.randint(1, 100))),
        ("121", "Sarah Brown", str(random.randint(1, 100))),
        ("122", "David Johnson", str(random.randint(1, 100))),
        ("123", "Sophia Garcia", str(random.randint(1, 100))),
        ("121", "James Martinez", str(random.randint(1, 100))),
        ("122", "Olivia Rodriguez", str(random.randint(1, 100))),
        ("123", "William Lee", str(random.randint(1, 100))),
        ("121", "Ava Walker", str(random.randint(1, 100))),
        ("122", "Isabella Hall", str(random.randint(1, 100))),
        ("123", "Liam Young", str(random.randint(1, 100))),
        ("121", "Mia Allen", str(random.randint(1, 100))),
        ("122", "Noah King", str(random.randint(1, 100))),
        ("123", "Charlotte Wright", str(random.randint(1, 100))),
        ("121", "Ethan Scott", str(random.randint(1, 100))),
        ("122", "Amelia Green", str(random.randint(1, 100))),
        ("123", "Lucas Adams", str(random.randint(1, 100))),
        ("121", "Harper Baker", str(random.randint(1, 100))),
        ("122", "Mason Gonzalez", str(random.randint(1, 100))),
        ("123", "Ella Nelson", str(random.randint(1, 100))),
        ("121", "Alexander Carter", str(random.randint(1, 100))),
        ("122", "Sofia Mitchell", str(random.randint(1, 100))),
        ("123", "Benjamin Perez", str(random.randint(1, 100))),
        ("121", "Aiden Roberts", str(random.randint(1, 100))),
        ("122", "Grace Turner", str(random.randint(1, 100))),
        ("123", "Jackson Phillips", str(random.randint(1, 100))),
        ("121", "Scarlett Campbell", str(random.randint(1, 100))),
        ("122", "Sebastian Parker", str(random.randint(1, 100))),
        ("123", "Victoria Evans", str(random.randint(1, 100))),
        ("121", "Matthew Edwards", str(random.randint(1, 100))),
        ("122", "Luna Collins", str(random.randint(1, 100))),
        ("123", "Daniel Stewart", str(random.randint(1, 100))),
        ("121", "Zoe Sanchez", str(random.randint(1, 100))),
        ("122", "Henry Morris", str(random.randint(1, 100))),
        ("123", "Chloe Rogers", str(random.randint(1, 100))),
    ]

    for student_data in students:
        add(*student_data)

    ui.show_menu()

if __name__ == "__main__":
    main()