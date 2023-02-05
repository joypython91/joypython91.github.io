from art import logo
import random

EASY_LEVEL_TERM = 10
HARD_LEVEL_TERM = 5
turns = 0
def check_answer(user_number, random_number, turns):
    if user_number > random_number:
      print("Too high.")
      return turns-1
    elif user_number < random_number:
      print("Too low.")
      return turns-1
    elif user_number == random_number:
      print("You win!")

def set_difficulty():
  user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if user_choice == "easy":
    return EASY_LEVEL_TERM
  else:
    return HARD_LEVEL_TERM

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm think you of a number between 1 and 100.")

  random_number = random.randint(1,100)
  print(f"The correct number is {random_number}")
  
  turns = set_difficulty()
  user_number = 0
  while user_number != random_number:
    print(f"You have {turns} attempts remaining to guess the number." )
  
    user_number = int(input("Make a guess: "))
  
    turns = check_answer(user_number, random_number, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif user_number != random_number:
      print("Guess again.")

game()