
class EnhancedString(str):
    """
    Enhanced string class with additional functionality.
    
    Inherits from the standard str class and adds methods for:
    - Finding repeating sequences
    - Checking if string is a palindrome
    """
    
    def has_repeating_sequences(self, s: str) -> bool:
        """
        Check if string contains repeating sequences of 3 or more characters.
        
        Args:
            s: String to check for repeating sequences
            
        Returns:
            bool: True if repeating sequences found, False otherwise
        """
        if len(s) < 6:  # minimum length needed for sequence repetition
            return False
            
        for i in range(len(s)-2):
            for j in range(i+3, len(s)-2):
                if s[i:i+3] == s[j:j+3]:
                    return True
        return False
        
    def is_palindrome(self) -> bool:
        """
        Check if string is a palindrome (reads the same forwards and backwards).
        
        Case-insensitive check, ignoring non-alphanumeric characters.
        Empty string is considered a palindrome.
        
        Returns:
            bool: True if string is palindrome, False otherwise
        """
        if not self:
            return True
            
        # Convert to lowercase and remove non-alphanumeric characters
        s = ''.join(char.lower() for char in self if char.isalnum())
        return s == s[::-1]

