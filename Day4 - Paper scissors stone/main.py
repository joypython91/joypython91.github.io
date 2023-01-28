import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

gamer_choice = input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.\n")

if gamer_choice == "0":
  print (rock)
elif gamer_choice == "1":
  print(paper)
elif gamer_choice == "2":
  print(scissors)
else:
  print("Please answer 0,1,2")

print("Computer chose:\n")
random_list = [rock, paper, scissors]
computer_choice = random.randint(0,2)
print(random_list[computer_choice])

if int(gamer_choice) == computer_choice:
  print("Fair, try again!")
elif int(gamer_choice) == 1 and computer_choice == 0:
  print("You win!")
elif int(gamer_choice) == 2 and computer_choice == 1:
  print("You win!")
elif int(gamer_choice) == 0 and computer_choice == 2:
  print("You win!")
elif int(gamer_choice) == 2 and computer_choice == 0:
  print("You lose!")
elif int(gamer_choice) == 0 and computer_choice == 1:
  print("You lose!")
elif int(gamer_choice) == 1 and computer_choice == 2:
  print("You lose!")
  