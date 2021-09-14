brands = [
    "Dell",
    "Apple",
    "HP",
    'Asus',
    'Acer',
]

seperator = " | "

output = seperator.join(brands)
print(output)

panagram = '''The quick brown
fox jumps over\tthe lazy dog'''

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
numbers = numbers.split(",")

for index in range(len(numbers)):
    numbers[index] = int(numbers[index])
print(numbers)
