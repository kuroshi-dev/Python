class Logger:
    """Logger class to handle logging messages with emojis."""
    def __init__(self):
        pass

    def print(self, message: str, emoji_type: str = None) -> None:
        """
        Print a message with optional emoji.

        Available emoji types:
            'succ'    (✅)  - Success message
            'err'     (❌)  - Error message
            'setup'   (🔧)  - Setup/configuration
            'folder'  (📁)  - Folder operations
            'check'   (✔️)  - Check/verification
            'exists'  (☑️ )  - Existence check
            'search'  (🔍)  - Search operations
            'edit'    (✏️)  - Edit operations
            'exit'    (🚪)  - Exit/termination
            'attent'  (❗)  - Attention message
            'warn'    (⚠️)  - Warning message
            'again'  (🔄)  - Repeat/loop message

        Args:
            message (str): The message to be printed
            emoji_type (str, optional): Type of emoji to prepend to message. Defaults to None.

        Returns:
            None: This method prints to stdout and doesn't return anything

        Note:
            If verbose mode is disabled, the message will be printed without emoji 
            regardless of the emoji_type parameter.
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
        }
        
        emoji = emojis.get(emoji_type, '')
        print(f"{emoji} {message}" if emoji else message)