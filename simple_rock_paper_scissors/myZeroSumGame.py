#Import lib
import random

#Import logo
from roPaSciLogo import rock, paper, scissors

gameImg = [rock, paper, scissors]

#User
userChoice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors.\n"))
if userChoice >= 3 or userChoice < 0:
    print("Too bad, you typed an invalid choice!")
else:
    print(gameImg[userChoice])

#Computer
    computerChoice = random.randint(0, 2)
    print("Computer is choosing: ")
    print(gameImg[computerChoice])

#If clauses
    if userChoice == 0 and computerChoice == 2:
        print("You win!")
    elif computerChoice == 0 and userChoice == 2:
        print("You lose!")
    elif computerChoice > userChoice:
        print("You lose!")
    elif userChoice > computerChoice:
        print("You win!")
    elif computerChoice == userChoice:
        print("It is a draw")
