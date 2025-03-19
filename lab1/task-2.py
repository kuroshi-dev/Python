import random as r

variables = { # here i test list for first time for myself
    "rand": r.randint(1, 100),
    "attempts": 0,
    "number": 0
}

def init(): # Initialization of the game
    """
    ## Initializes the game
    Shows the welcome message and the rules of the game.
    """
    print("Task 2: Number Guessing Game")
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    print("Can you guess what it is?")
    print("Good luck!")
    print("© by Bulyukin Volodymyr")
    print("")
init()

def maketry():
    """
    Prompts the user to make a guess
    """
    variables["number"] = int(input("Guess a number from 1 to 100: "))
    if variables["number"] < 1 or variables["number"] > 100: # Validation and cycle using functions
        print("Number is out of range!")
        maketry()
        
def check_guess():
    """
    Checks if the guess is correct
    and updates the number of attempts
    """
    if variables["number"] == variables["rand"]: 
        update_attempts("correct") # mb better use bool instead of string, but it looks better, i can upscale this game then with more inputs on attemps status:)
    elif variables["number"] < variables["rand"]:
        print("Number is Higher!")
        update_attempts("wrong") 
    elif variables["number"] > variables["rand"]:
        print("Number is Lower!")
        update_attempts("wrong")

def update_attempts(result):
    """
    Updates the number of attempts
    """
    variables["attempts"] += 1 # Increment the number of attempts
    if result == "wrong":
        maketry(); check_guess()
    elif result == "correct":
        print(f"Congratulations! You guessed the number in {variables["attempts"]} attempts!") # then i got something like exit(), cause func not called anymore

maketry(); check_guess() # Make the first guess, then check it