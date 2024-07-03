workout_dict = {
    'A':'20 burpees with jump',
    'B':'20 squats',
    'C':'20 pushups',
    'D':'10 pull ups',
    'E':'25 situps',
    'F':'20 lunges(10 ea. leg)',
    'G':'20 dips',
    'H':'1 minute wall sit',
    'I':'30 high knees',
    'J':'10 jump squats',
    'K':'50 mountain climbers',
    'L':'60 second plank',
    'M':'10 Diamond pushups',
    'N':'30 Russion twists',
    'O':'10 Pistol Squats (10 ea. leg)',
    'P':'10 Truck jumps',
    'Q':'30 Scissor kicks',
    'R':'1 minute side plank (30s ea. side)',
    'S':'20 Tyson pushups',
    'T':'10 Navy Seal burpees',
    'U':'10 Chin ups',
    'V':'20 Toe touches',
    'W':'20 Bicycle crunches',
    'X':'2 minute jump rope',
    'Y':'20 V-ups',
    'Z':'30 Crunches',
    }


def get_name():
    """Recieve the users name."""
    
    name = input("Enter your name: ")
    print("Your name is: " + name)
    return name


''' Version1 name_letters'''
def name_letters(name):
    """Single out the letters of the name into a dictionary."""
    name_letters = []    
    for ele in name.upper():
        if ele.isalpha():  # Skip spaces and non-alphabet characters
            name_letters.append(ele)
    print("The letters in your name are :\n "+ str(name_letters))
    return name_letters


''' Version3 generate_workout'''
def generate_workout(workout_dict, name_letters):
    """Creates a Workout customized to the user's name."""
    print("\nYour workout based on your name:")
    for letter in name_letters:
        workout = workout_dict.get(letter)
        if workout:
            print(f"{letter}: {workout}")
        else:
           print(f"{letter}: No workout defined for this letter")
    return



name = get_name()
letters = name_letters(name)
generate_workout(workout_dict, letters)


