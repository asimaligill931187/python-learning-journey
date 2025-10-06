# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
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
player=input("Enter 1 for rock and 2 for Paper and 3 Scissor??").lower()
if player=="1":
    player='rock'
elif player=="2":
    player="paper"
elif player=="3":
    player="scissors"
else:
    print("wrong choice")


# 
# 
computer=["rock", "paper", "scissors"]
computer_choice=random.choice(computer)
if player == computer_choice:
    print("It's a draw!")
elif (player == "rock" and computer_choice == "scissors") or \
     (player == "scissors" and computer_choice == "paper") or \
     (player == "paper" and computer_choice == "rock"):
    print(f"player choice:{player}")
    print(f"computer choice:{computer_choice}")
    print("You win!")
   
else:
    print("You lose!")