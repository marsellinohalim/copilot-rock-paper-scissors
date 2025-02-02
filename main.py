import random

valid_arg = ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']

def get_user_choice():
    while True:
        user_choice = str(input("Please choose, rock, paper, scissors, lizard, spock: ")).upper()
        if validate_user_choice(user_choice):
            return user_choice
        else:
            print("Invalid choice, please input again...")

def validate_user_choice(user_choice):
    return user_choice in valid_arg

def get_computer_choice():
    comp_choice_rand = random.randint(0, 4)
    return valid_arg[comp_choice_rand]

def determine_winner(user_choice, comp_choice):
    winning_choices = {
        'ROCK': ['SCISSORS', 'LIZARD'],
        'PAPER': ['ROCK', 'SPOCK'],
        'SCISSORS': ['PAPER', 'LIZARD'],
        'LIZARD': ['SPOCK', 'PAPER'],
        'SPOCK': ['SCISSORS', 'ROCK']
    }

    if user_choice == comp_choice:
        return "It's a tie"
    elif comp_choice in winning_choices[user_choice]:
        return "The winner is: user"
    else:
        return "The winner is: computer"

def main():
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()

    print("The computer chose: " + comp_choice)
    print("The user chose: " + user_choice)
    print(user_choice + " vs " + comp_choice)

    winner = determine_winner(user_choice, comp_choice)
    print(winner)

if __name__ == "__main__":
    main()