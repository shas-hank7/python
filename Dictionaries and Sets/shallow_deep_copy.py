from contents import recipes


def my_deepcopy(d: dict) -> dict:
    newDict = {}
    for food in recipes:
        newDict[food] = recipes[food].copy()
    return newDict


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])

print(recipes_copy)
