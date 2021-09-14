from contents import pantry, recipes

newItemsDict = {}

def addToList(item, quantity):
    # if item in newItemsDict:
    #     newItemsDict[item] += quantity
    # else:
    #     newItemsDict[item] = quantity
    newItemsDict[item] = newItemsDict.setdefault(item, 0) + quantity

nexDict = {}

for index, item in enumerate(recipes):
    nexDict[str(index+1)] = item

choice = None

while True:
    print("Please select a recipe")
    print("----------------------")
    for key, item in nexDict.items():
        print(f"{key} - {item}")
    
    choice = input(": ")
    if choice=="0":
        break
    elif choice in nexDict:
        selectedItem = nexDict[choice]
        print(f"You have selected {selectedItem}")
        ingredients = recipes[selectedItem]
        for foodItem, required_quantity in ingredients.items():
            quantityInPantry = pantry.get(foodItem, 0)
            if required_quantity<=quantityInPantry:
                print(f"\t{foodItem.upper()} - OK")
            else:
                quantityToBuy = required_quantity - quantityInPantry
                print(f"\tYou need to buy {quantityToBuy} of {foodItem.upper()}")
                addToList(foodItem, quantityToBuy)
                

for items, quantity in newItemsDict.items():
    print(items.upper(), quantity, sep=" - ")
