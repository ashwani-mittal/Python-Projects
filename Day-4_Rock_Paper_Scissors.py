#!/usr/bin/env python
# coding: utf-8

# In[10]:


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
import random

options = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,len(options)-1)
if user_choice >=3 or user_choice < 0:
    print("You entered an invalid input. You Lose!")   
else:    
    print("You chose: \n" + options[user_choice])
    print("Computer chose: \n" + options[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You Win!")
    elif user_choice < computer_choice:
        print("You Lose!")
    elif user_choice == computer_choice:
        print("It's a Draw!")

