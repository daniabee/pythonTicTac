import random

while True:

  user_choice = input("Are you choosing rock, paper, or scissors?: ")

  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)

  print(f"\nYou chose {user_choice}, the computer chose {computer_choice}.\n")

  if user_choice == computer_choice: 
    print(f"You tied!")
  elif user_choice == "rock": 
    if computer_choice == "scissors":
      print("Rock smashes scissors! You win!")
    else: 
      print("Paper covers rock! You lose.")
  elif user_choice == "paper":
    if computer_choice == "rock":
      print("Paper covers rock! You win!")
    else:
      print("Scissors cuts paper! You lose.")
  elif user_choice == "scissors":
    if computer_choice == "paper":
      print("Scissors cuts papper! You win!")
    else:
      print("Rock smashes scissors! You lose.")

  play_again = input("Play again? (y/n): ")
  if play_again.lower() != "y":
    break 

