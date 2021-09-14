import random
ul = 1000
answer = random.randint(1, ul)
#print(answer)       #TODO: Remove after testing.


# guess = int(input("Enter a number"))
#
# if guess == answer:
#     print("You guessed it")
# else:
#     if guess < answer:
#         print("Guess a higher number")
#     else:
#         print("Guess a lower number")
#     guess = int(input("Enter a number"))
#     if guess == answer:
#         print("Congrats!")
#     else:
#         print("You couldn't guess the number correctly :\\")

# guess = int(input("Enter a number between 1 and {}\n".format(ul)))
#
# i = 1
#
# while guess != answer:
#     if guess > answer:
#         print("Oops! You should have guessed a lower number")
#     elif guess == 0:
#         print("Game over")
#         break
#     else:
#         print("Oops! You should have guessed a higher number")
#     guess = int(input("Guess another number\n"))
#     i += 1
#
# if guess != 0:
#     print("You guessed it in {} attempts".format(i))

hi = 1000
lo = 1
i = 1

print("Enter a number between {} and {}".format(lo, hi))
input("Press Enter to begin")

while hi != lo:
    guess = ((lo + ((hi - lo) // 2)))
    print("Current guess is {}".format(guess))
    dir = input().casefold()

    if dir == "h":
        lo = guess + 1
        i += 1
    elif dir == "l":
        hi = guess - 1
        i += 1
    elif dir == "c":
        i += 1
        break
    else:
        print("Please enter valid keywords")
    print("High is {} and low is {}".format(hi, lo))

else:
    print("The computer got it in {} attempts".format(i))

