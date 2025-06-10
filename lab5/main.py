from models import TaskManager
from interface import UserInterface

def main():
    manager = TaskManager()
    ui = UserInterface(manager)
    ui.show_menu()

if __name__ == "__main__":
    main()