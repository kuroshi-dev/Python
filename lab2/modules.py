import random as r

def show_season(month):
    """This function takes a month number (1-12) and prints the corresponding season and month name.
    
    Args:
        month (int): Month number (1-12).
        
    Returns:
        list: A list of seasons.
    """
    
    seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    if month in [12, 1, 2]:
        print(f"Month: {months[month - 1]}, Season: {seasons[0]}") 
        # Winter
    elif 3 <= month <= 5:
        print(f"Month: {months[month - 1]}, Season: {seasons[1]}") 
        # Spring
    elif 6 <= month <= 8:
        print(f"Month: {months[month - 1]}, Season: {seasons[2]}")
        # Summer
    elif month in [9, 10, 11]:
        print(f"Month: {months[month - 1]}, Season: {seasons[3]}") 
        # Autumn
    else:
        print("Invalid month")
    return seasons

def is_leap_year(year) -> bool:
    """Checks if a given year is a leap year.
    
    Args:
        year (int): The year to check.
        
    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # Leap year condition
        return True
    return False

def is_valid_date(day: int, month: int, year: int) -> bool:
    """
    Checks if a given date is valid.
    
    Args:
        day (int): Day of the month.
        month (int): Month number.
        year (int): Year.
        
    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # Check basic constraints
    if not (1 <= month <= 12) or year < 1 or day < 1:
        return False
        

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # List of days in each month
  
    if is_leap_year(year):
        days_in_month[1] = 29
  
    return day <= days_in_month[month - 1] # Check if day is within the valid range for the month

def find_duplicate_dates(dates: list) -> list:
    """
    Finds duplicate dates in a list.
    
    Args:
        dates (list): List of dates in the format dd.mm.yyyy.
        
    Returns:
        list: List of duplicate dates.
    """
    seen = set()
    duplicates = set()
    
    for date_str in dates:
        try: # Split the date string into day, month, and year
            day, month, year = map(int, date_str.split('.'))
           
            if is_valid_date(day, month, year): # Check if the date is valid
                if date_str in seen:
                    duplicates.add(date_str)
                else:
                    seen.add(date_str)
            else:
                print(f"❌ Invalid date: {date_str}")
                
        except ValueError: # Handle invalid date formats
            print(f"❌ Incorrect date format: {date_str}")
            continue
            
    return list(duplicates)

def generate_random_date() -> str:
    """
    Generates a random valid date.
    
    Returns:
        str: A random date in the format dd.mm.yyyy
    """

    year = r.randint(1900, 2024)
    month = r.randint(1, 12)

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # List of days in each month
    if is_leap_year(year):
        days_in_month[1] = 29

    max_days = days_in_month[month - 1]
    day = r.randint(1, max_days)

    return f"{day:02d}.{month:02d}.{year}" # Format the date as dd.mm.yyyy

def show_menu():
    """Displays the menu of available functions."""
    menu_options = [
        "✨ 1. Determine the season by month number",
        "🌟 2. Check if a year is a leap year",
        "📅 3. Check if date exists",
        "🔍 4. Find duplicate dates",
        "🎲 5. Generate random date",
        "❌ 0. Exit"
    ]
    print("\nLab 2 by Buliukin Volodimir | Group: KN-24 | Variant: 3")
    print("\n.・。.・゜✭・.・✫・゜・。.・゜✭・.・")
    for option in menu_options:
        print(f"  ✧ {option}")
    print(".・。.・゜✭・.・✫・゜・。.・゜✭・.・ ")


def ask_to_continue() -> bool:
    """
    Asks the user if they want to continue executing the function.
    
    Returns:
        bool: True if the user wants to continue, False otherwise.
    """
    again = input("🔄 Do you want to call this function again? (y/n): ").strip().lower()
    return again == "y"