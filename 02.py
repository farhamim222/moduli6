import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():

    sides = int(input("Enter the number of sides on the die: "))
    roll = 0

    while roll != sides:
        roll = roll_dice(sides)
        print(f"Dice rolled: {roll}")

main()
