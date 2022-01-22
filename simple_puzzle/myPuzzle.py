#Import logo
from treasureLogo import logo

print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Choosing paths
choice1 = input('You\'re at a cross road. Where do you want to go? Type "north" or "south" \n').lower()
if choice1 == "north":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There are 3 houses. One with the red door, one with the yellow door and last one with the blue door. Which house do you choose? \n").lower()
    if choice3 == "red":
      print("It's a house full of drunken pirates. You die!.")
    elif choice3 == "yellow":
      print("Oh yeah, you found the treasure! You are rich!")
    elif choice3 == "blue":
      print("You enter a empty house! Uh-oh! It is full of traps. You die!.")
    else:
      print("You chose to run away ? Coward!.")
  else:
    print("You get attacked by an angry crocodile. You are pieces of meat now!.")
else:
  print("You are lost!.")