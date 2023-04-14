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

options = [rock, paper, scissors]
user_choice = int(input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user_choice = options[user_choice]
print(user_choice)
computer_choice = random.choice(options)
print(f"computer chose: {computer_choice}")

if (user_choice == computer_choice):
  print("Draw")
elif((user_choice == "rock" and computer_choice == "scissors")\
    or (user_choice == "paper" and computer_choice == "rock")\
    or (user_choice == "scissor" and computer_choice == "paper")):
  print("You win")
else:
  print("You lose")