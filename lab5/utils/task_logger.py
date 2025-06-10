class TaskLogger:
    """
    Class to handle logging messages with emojis.
    
    This class provides functionality to print messages with optional emoji prefixes
    for different types of log messages like success, error, warning etc.

    ----------------------------------------

    Methods:
        print(message: str, emoji_type: str = None): Prints a message with optional emoji

    Available emoji types:
        'succ'    (✅) - Success message
        'err'     (❌) - Error message 
        'setup'   (🔧) - Setup/configuration
        'folder'  (📁) - Folder operations
        'check'   (✔️) - Check/verification
        'exists'  (☑️) - Existence check
        'search'  (🔍) - Search operations
        'edit'    (✏️) - Edit operations
        'exit'    (🚪) - Exit/termination
        'attent'  (❗) - Attention message
        'warn'    (⚠️) - Warning message
        'again'   (🔄) - Repeat/loop message

    Examples:
        >>> logger = Logger()
    >>> logger.print("Operation successful", "succ")
        ✅ Operation successful
    >>> logger.print("An error occurred", "err") 
        ❌ Error: An error occurred

    Note:
        Messages are printed to stdout with emoji prefixes when emoji_type is specified
    """
    def __init__(self):
        """Initialize Logger instance.

        ----------------------------------------

        Sets up the emoji dictionary for message formatting.
        """
        pass

    def print(self, message: str, emoji_type: str = None) -> None:
        """
        Print a message with optional emoji prefix.

        This method prints the given message to stdout, optionally prefixing it
        with an emoji based on the specified emoji type.

        ----------------------------------------

        Args:
            message (str): The message to be printed
            emoji_type (str, optional): Type of emoji to prepend to message.
                                      Defaults to None.

        Returns:
            None: This method prints to stdout

        Side Effects:
            - Prints formatted message to console

        Note:
            If emoji_type is not recognized, message is printed without emoji

        Examples:
            >>> logger = Logger()
            >>> logger.print("Operation successful", "succ")
            ✅ Operation successful
            >>> logger.print("File not found", "err")
            ❌ Error: File not found
            >>> logger.print("Regular message")
            Regular message
        """

        emojis = {
            'succ': '✅',
            'err': '❌ Error: ',
            'setup': '🔧',
            'folder': '📁',
            'check': '✔️ ',
            'exists': '☑️ ',
            'again': '🔄',
            'search': '🔍',
            'edit': '✏️ ',
            'exit': '🚪',
            'attent': '❗',
            'warn': '⚠️',
            'task_created': '📝',
            'task_assigned': '👤',
            'status_update': '📊',
            'task_info': '📖',
            'string_op': '🔤',
            'menu': '📋',
            'input': '✨',
            'info': 'ℹ️'
            
        }
        
        emoji = emojis.get(emoji_type, '')
        print(f"{emoji} {message}" if emoji else message)