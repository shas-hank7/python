# computer_parts = ["computer",
#                   "monitor",
#                   "keyboard",
#                   "mouse",
#                   "mouse mat"]
#
# for part in computer_parts:
#     print(part)
#
# print(computer_parts[0::2])
#
# a = b = 12
#
# a += 1
# print(a)
# print(b)
#
# another_list = computer_parts
# computer_parts += ["UPS"]
# print(id(computer_parts))
# print(id(another_list))
# print(computer_parts)
# print(another_list)
#
# a = b = c = d = another_list
# another_list + = ["UPS"]
# print(c)

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# another_even = even
#
# even.extend(odd)
#
# print(even)
# even.sort(reverse=True)
# print(even)
# print(another_even)
#
# even = str(even)
# print(even)
# if :
#     print("Hello")
#
# computer_parts = ["computer",
#                   "monitor",
#                   "keyboard",
#                   "mouse",
#                   "mouse mat",
#                   "speakers",
#                   ]
#
# print(computer_parts)
# computer_parts[2:] = ["HDMI Cable", "Speakers"]
# print(computer_parts)

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

for meal in menu:
    if "spam" not in meal:
        print(meal)
    else:
        print("{} meal has a spam score of {}".format(meal, meal.count("spam")))

