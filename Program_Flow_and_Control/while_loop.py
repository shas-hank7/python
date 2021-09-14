# i = 0
# while i <= 10:
#     print(i)
#     i += 1
#
# available_exits = ["north", "south", "east", "west"]
#
# while True:
#     chosen_exit = input("Choose a direction: ")
#     chosen_exit = chosen_exit.lower()
#     if chosen_exit in available_exits:
#         print("Aren't you glad you got out of there")
#         break
#     elif chosen_exit == "quit":
#         print("Game over")
#         break
#     else:
#         print("That won't get you outta here")

available_exits = ["north", "south", "east", "west"]
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == "quit":
        print("Game Over")
        break
else:
    print("Aren't you glad you got out of there")



