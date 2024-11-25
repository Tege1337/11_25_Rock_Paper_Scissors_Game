import random

choices = ["rock", "paper", "scissors"]

while True:
        
    user_choice = input("Rock, Paper or Scissors?: ").lower()
    opponent_choice = random.choice(choices).lower()

    a = user_choice
    b = opponent_choice

    # Tie
    if a == b:
        print(f"It's a tie! You both chose {a}")

    # Win
    if a == "SCISSORS" and b == "PAPER":
        print(f"You won! You chose {a}, and the opponent chose {b}!")
    if a == "PAPER" and b == "ROCK":
        print(f"You won! You chose {a}, and the opponent chose {b}!")
    if a == "ROCK" and b == "SCISSORS":
        print(f"You won! You chose {a}, and the opponent chose {b}!")

    # Lose
    if b == "SCISSORS" and a == "PAPER":
        print(f"You lost! You chose {a}, and the opponent chose {b}!")
    if b == "PAPER" and a == "ROCK":
        print(f"You lost! You chose {a}, and the opponent chose {b}!")
    if b == "ROCK" and a == "SCISSORS":
        print(f"You lost! You chose {a}, and the opponent chose {b}!")