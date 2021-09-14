import random


def getInteger():
    """
    Gets an integer from Standard Input (stdin).
    The function will continue looping, until a valid `int` is entered.

    Returns:
        int: The integer that the user enters.
    """
    while True:
        temp = input()
        if temp.isnumeric():
            return int(temp)
        else:
            print("Invalid value eneterd! Please try again: ")


ul = 1000
answer = random.randint(1, ul)

i = 1

print("Please guess a number:")
invalid = "Inavlid value eneterd! Please try again: "
guess = getInteger()

while guess != answer:
    if guess > answer:
        print("Oops! You should have guessed a lower number. Try again:")
    elif guess == 0:
        print("Game over")
        break
    else:
        print("Oops! You should have guessed a higher number. Try again:")
    guess = getInteger()
    i += 1

if guess != 0:
    print("You guessed it in {} attempts".format(i))

