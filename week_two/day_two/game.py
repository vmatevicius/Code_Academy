# create a number guessing game from 1-10, with random library. (IDEA FOR LATER MAYBE)
import random

print("Welcome to guessing game! You have to guess the correct number in 3 tries!")

random_int = random.randint(1,2)

tries = 3

while tries != 0:
    try:
        number = int(input("Guess the number!: "))
        tries = tries - 1
        if number == random_int:
            tries += 1
            print("Correct! The number was:",random_int)
            break
        else:
            print("Wrong! Try again!")
            if number > random_int:
                print("The correct answer is lower than your current answer")
            else:
                print("The correct answer is higher than your current answer")
            print("Tries left:", tries)
    except ValueError:
        print("Must input a number")
        pass   
if tries == 0:
    print("Answer was:", random_int)