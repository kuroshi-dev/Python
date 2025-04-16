from modules import *

def main():
    print("""
          \nI recommend to start program in not default terminal
          to see the full output of the program.
          """)
    
    while True:
        
        show_menu()
        choice = input("Please select a menu option: ") # Get user input for menu choice
      
        if choice == "0":
            print("🚪: Program terminated!")
            break
            
        elif choice == "1": # Determine the season by month number
            while True:
                try:
                    month = int(input("Enter the month number (1-12): ")) # Get user input for month
                    show_season(month)
                except ValueError:
                    print("❌ Error: please enter a valid number")
                
                if not ask_to_continue(): break
        elif choice == "2": # Check if a year is a leap year
            while True:
                try:
                    year = int(input("Enter the year: "))
                    if is_leap_year(year):
                        print(f"✅ {year} is a leap year.")
                    else:
                        print(f"❌ {year} is not a leap year.")
                except ValueError:
                    print("❌ Error: Please enter a valid year.")
                
                if not ask_to_continue(): break
        elif choice == "3": # Check if date exists
            while True:
                try:
                    day = int(input("Enter day: ")) 
                    month = int(input("Enter month: "))
                    year = int(input("Enter year: "))
                    
                    if is_valid_date(day, month, year): # Check if date is valid
                        print(f"✅ Date {day}.{month}.{year} exists!")
                    else: #
                        print(f"❌ Date {day}.{month}.{year} does not exist!")
                except ValueError:
                    print("❌ Error: Please enter valid numbers")
                
                if not ask_to_continue(): break
        elif choice == "4": # Find duplicate dates
            while True:
                print("\nEnter dates in the format dd.mm.yyyy")
                print("To finish entering, leave the input blank\n")
                
                dates = [] # Initialize an empty list to store dates
                while True:
                    date = input("Enter a date: ").strip()
                    if not date:
                        break
                    dates.append(date)
                
                if dates:
                    duplicates = find_duplicate_dates(dates)
                    if duplicates:
                        print("\n✅ Duplicate dates found:")
                        for date in duplicates:
                            print(f"  📅 {date}")
                    else:
                        print("\n✨ No duplicate dates found")
                else:
                    print("❌ The list of dates is empty")

                if not ask_to_continue(): break 
        elif choice == "5":
            while True:
                random_date = generate_random_date()
                print(f"\n🎲 Generated random date: {random_date}")
                
                if not ask_to_continue(): break
        else:
            print("⚠️ Error: Please select a valid menu option.") # Invalid menu option
        
if __name__ == "__main__": # Entry point of the program
    main()