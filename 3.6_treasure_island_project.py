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
game_over = False
continue_game = True

def decision_1():
    decision_1_input = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\":\n").lower()

    if (decision_1_input == "left"):
        decision_2()

    elif (decision_1_input == "right"):
        print("Game Over.")

    else:
        print("Invalid Option entered.  Please Try again")
        decision_1()

def decision_2():
    decision_2_input = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across?:\n").lower()

    if (decision_2_input == "wait"):
        decision_3()

    elif (decision_2_input == "swim"):
        print("Game Over.")

    else:
        print("Invalid Option entered.  Please Try again")

def decision_3():
    decision_3_input = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? Red, Blue, or Yellow:\n").lower()

    if (decision_3_input == "yellow"):
        print("You Win!")

    elif (decision_3_input == "red" or decision_3_input == "blue"):
        print("Game Over.")

    else:
        print("Invalid Option entered.  Please Try again")
        decision_3()

decision_1()
