# name = input("Please Enter your name\n")
# age = int(input("How old are you, {}\n".format(name)))
#
# if age > 18:
#     print("You can vote, {}".format(name))
#     print("You are also eligible for a DL")
# elif age == 18:
#     print("You are 18")
# else:
#     print("Please come back in {} years".format(18-age))
#
# name1 = input("Tree1")
# name2 = input("Tree2")
#
# if name1 == name2:
#     print("Same")

#Guess Game

# answer = 5
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

# age = int(input("How old are you"))
#
# if 18 <= age <= 65:
#     print("Get a job you piece of shit!")
# else:
#     print("You don't have to work as of now")
#
# print("-" * 80)
# if age < 16 or age > 65:
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")

# day = "Saturday"
# temp = 30
# raining = False
#
# if day == "Saturday" and temp > 27 and not raining:
#     print("Go for a swim.")
# else:
#     print("The conditions are unfavourable for a swim. Learn Python instead.")

# activity = input("What would you like to do today\n")
#
# if "cinema" not in activity.casefold():
#     print("But I want to go to cinema")
# else:
#     print("Lets go to cinema")

name = input("Enter your name")
age = int(input("Enter your age"))

if 18<=age<31:
    print("Welcome")
else:
    print("Chala ja")