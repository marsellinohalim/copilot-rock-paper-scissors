import random
from fastapi import FastAPI
import uvicorn
app = FastAPI()

valid_arg = ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']

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

@app.post("/play")
def play_game(user_choice: str):
    if validate_user_choice(user_choice):
        comp_choice = get_computer_choice()

        result = {
            "computer_choice": comp_choice,
            "user_choice": user_choice,
            "winner": determine_winner(user_choice, comp_choice)
        }

        return result
    else:
        return {"error": "Invalid choice"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)