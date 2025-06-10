class TaskManager:
    """
    A class for managing tasks and their executors.
    
    This class provides functionality for creating tasks, assigning them to workers,
    tracking task progress, and getting task information.
    
    Attributes:
        tasks (dict): Dictionary storing tasks with their details
    """
    
    def __init__(self):
        """Initialize empty task manager"""
        self.tasks = {}
        
    def create_task(self, task_name: str, description: str = "") -> None:
        """
        Create a new task with given name and description.
        
        Args:
            task_name: Name/identifier of the task
            description: Detailed description of the task (optional)
        """
        self.tasks[task_name] = {
            "description": description,
            "assignee": None,
            "status": "new"
        }
        
    def assign_task(self, task_name: str, assignee: str) -> None:
        """
        Assign a task to a worker.
        
        Args:
            task_name: Name of the task to assign
            assignee: Name of the worker to assign the task to
            
        Raises:
            ValueError: If task_name doesn't exist
        """
        if task_name in self.tasks:
            self.tasks[task_name]["assignee"] = assignee
            self.tasks[task_name]["status"] = "assigned"
        else:
            raise ValueError("Task not found")
            
    def update_status(self, task_name: str, status: str) -> None:
        """
        Update the status of a task.
        
        Args:
            task_name: Name of the task to update
            status: New status for the task
            
        Raises:
            ValueError: If task_name doesn't exist
        """
        if task_name in self.tasks:
            self.tasks[task_name]["status"] = status
        else:
            raise ValueError("Task not found")
            
    def get_task_info(self, task_name: str) -> dict:
        """
        Get detailed information about a task.
        
        Args:
            task_name: Name of the task to get info about
            
        Returns:
            dict: Dictionary containing task details
            
        Raises:
            ValueError: If task_name doesn't exist
        """
        if task_name in self.tasks:
            task = self.tasks[task_name]
            return {
                "task": task_name,
                "description": task["description"],
                "assignee": task["assignee"],
                "status": task["status"]
            }
        else:
            raise ValueError("Task not found")

    def get_all_tasks(self) -> dict:
        """
        Get a dictionary of all tasks with their details.
        
        Returns:
            dict: Dictionary containing all tasks and their details
        """
        return self.tasks
