options = ["Learn Python", "Learn Java", "Go swimming", "Have Dinner", "Go to bed", "Exit"]

while True:
    i = 1

    print("Please choose your iption from the list")
    for option in options:
        if option != "Exit":
            print("{}. {}".format(i, option))
            i += 1
    print("0. Exit")
    #print(i)



    choice = int(input())

    if choice in range(1 , i):
        print("You chose option number {} which is {}".format(choice, options[choice-1]))
        break
    elif choice == 0:
        print("Loop Successfully Terminated!")
        break
    else:
        print("You chose an invalid option")

