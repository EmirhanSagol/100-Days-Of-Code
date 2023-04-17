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
pics= [rock, paper, scissors]

player_choice = int(input("What to you choice? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if player_choice < 0 or player_choice > 2:
    print("Don\'t enter numbers out of scope!'")
    exit()

computer_choice = random.randint(0, 2)
print(f"{pics[player_choice]}\nComputer choice:\n{pics[computer_choice]}")

if (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
    print("You Win!")
elif (player_choice == 2 and computer_choice == 0) or (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2):
    print("You Lose!")
else:
    print("It is a draw!")