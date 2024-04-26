import random

def get_choices():
    player_choice=input("enter a choice (rock, paper, scissors): ")
    options=["rock", "paper", "scissors"]
    computer_choice=random.choice(options)
    choices={"player choice" : player_choice, "computer choice" : computer_choice}
    return choices


