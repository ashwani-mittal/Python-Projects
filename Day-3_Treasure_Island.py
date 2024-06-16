#!/usr/bin/env python
# coding: utf-8

# In[2]:


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
path = input('''You're at a cross road. Where do you want to go? Type "left" or "right"\n''').lower()
if path == 'left':
    boat = input('''You've reached a lake. You see a island in the middle of the lake. Type "wait" to wait for the boat or "swim" to swin across.\n''').lower()
    if boat == 'wait':
        door = input('''You finally reach the island. There is a house. Inside the house you see 3 rooms with doors of different colors: One red, One yellow and one green. Which door do you pick? Type "red", "yellow" or "green".\n''').lower()
        if door == 'green':
            print("You found the treasure. YOU WIN!!!")
        elif door == 'yellow':
            print("The room inside is a maze of underground tunnels that leads to a trap. GAME OVER!!!")
        else:
            print("It's fire everywhere. GAME OVER!!!")
    else:
        print("You just entered a lake full of nasty piranhas that attacked you. GAME OVER!!!")

else:
    print("A hungry wild Tiger jumped at you from the bushes. GAME OVER!!!")

