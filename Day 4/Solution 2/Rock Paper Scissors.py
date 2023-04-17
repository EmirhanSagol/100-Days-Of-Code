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
pics = [rock, paper, scissors]
 
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if your_choice < 0 or your_choice > 2 :
  print("Don\'t enter numbers out of scope!'")
  exit()
 
print(pics[your_choice])
 
comp_choice = random.randint(0,2)
print(f"Computer chose:\n{pics[comp_choice]}")
 
choice_matrix = [ ["It\'s a draw", "You lose", "You win"], ["You win", "It\'s a draw", "You lose"], ["You lose", "You win", "It\'s a draw"] ]
print(choice_matrix[your_choice][comp_choice])