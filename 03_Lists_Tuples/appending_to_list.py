available_parts = ["Monitor",
                   "CPU",
                   "Keyboard",
                   "Mouse",
                   "Mouse Mat",
                   "HDMI Cable",
                   "UPS",
                   "Speakers"]
current_choice = -1
computer_parts = []

while current_choice != 0:
    if current_choice in range(1, len(available_parts)+1):
        if available_parts[current_choice-1] not in computer_parts:
            print("Adding {}".format(available_parts[current_choice-1]))
            computer_parts.append(available_parts[current_choice-1])
        else:
            print("Removing {}".format(available_parts[current_choice-1]))
            computer_parts.remove(available_parts[current_choice-1])
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add a valid option")
        for number, part in enumerate(available_parts):
            print("{}: {}".format(number+1, part))
    current_choice = int(input())
print(computer_parts)

# data = [
#     "Andromeda - Shrub",
#     "Bellflower - Flower",
#     "China Pink - Flower",
#     "Daffodil - Flower",
#     "Evening Primrose - Flower",
#     "French Marigold - Flower",
#     "Hydrangea - Shrub",
#     "Iris - Flower",
#     "Japanese Camellia - Shrub",
#     "Lavender - Shrub",
#     "Lilac - Shrub",
#     "Magnolia - Shrub",
#     "Peony - Shrub",
#     "Queen Anne's Lace - Flower",
#     "Red Hot Poker - Flower",
#     "Snapdragon - Flower",
#     "Sunflower - Flower",
#     "Tiger Lily - Flower",
#     "Witch Hazel - Shrub",
# ]
#
# flowers = []
# shrubs = []
#
# # write your code here
# for plant in data:
#     if "Shrub" in plant:
#         shrubs.append(plant.replace(" - Shrub", ""))
#     else:
#         flowers.append(plant.replace(" - Flower", ""))
# print(flowers)
# print(shrubs)