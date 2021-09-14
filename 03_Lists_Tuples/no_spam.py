menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# for meal in menu:
#     for index in range(len(meal)-1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
#     print(meal)

for meal in menu:
    for index, food in enumerate(meal):
        if food == "spam" and index == 0:
            print(end="")
        elif food == "spam":
            continue
        if index != 0:
            print(end=", ")
        print(food, end="")
    print()