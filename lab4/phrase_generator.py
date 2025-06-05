import random

def generate_random_phrase():
    """
    Generates a random Ukrainian phrase consisting of an adjective, a noun, and a verb.
    The function randomly selects a noun (with its grammatical gender), a verb, and an adjective (with masculine, feminine, and neuter forms).
    It matches the adjective form to the gender of the noun and constructs a phrase in the format: "<adjective> <noun> <verb>".
    Returns:
        str: A randomly generated phrase in Ukrainian.
    """
    
    nouns = [ # List of nouns
        ("кіт", "m"), ("сонце", "n"), ("будинок", "m"), ("комп'ютер", "m"), 
        ("книга", "f"), ("дерево", "n"), ("море", "n"), ("місто", "n")
    ]
    
    verbs = ["спить", "світить", "стоїть", "працює", "лежить", "росте", "шумить", "живе"]
    
    adjectives = [ # List of adjectives with their forms
        ("гарний", "гарна", "гарне"),
        ("яскравий", "яскрава", "яскраве"),
        ("великий", "велика", "велике"),
        ("швидкий", "швидка", "швидке"),
        ("цікавий", "цікава", "цікаве"),
        ("зелений", "зелена", "зелене"),
        ("синій", "синя", "синє"),
        ("гучний", "гучна", "гучне")
    ]
    
    noun, gender = random.choice(nouns)
    verb = random.choice(verbs)
    adj_forms = random.choice(adjectives)

    if gender == "m": # masculine
        adj = adj_forms[0]
    elif gender == "f": # feminine
        adj = adj_forms[1]
    else:  # neutral
        adj = adj_forms[2]
    
    return f"{adj} {noun} {verb}" # Generate a random phrase

def main():
    print("Генератор випадкових фраз")
    print("-" * 30)

    for i in range(5): # Generate 5 random phrases
        phrase = generate_random_phrase()
        print(f"Фраза {i+1}: {phrase}")

if __name__ == "__main__":
    main()