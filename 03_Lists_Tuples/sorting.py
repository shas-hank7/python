pangram = "The quick brown fox jumps over the lazy dog"

print(pangram)
letters = sorted(pangram)
print(letters)

numbers = [2, 4, 6, 8, 1, 3, 5, 7, 9]
more_numbers = numbers
more_more_numbers = list(numbers)
extra_numbers = numbers.copy()

print(numbers is more_numbers)
print(numbers is more_more_numbers)
print(numbers is extra_numbers)

characters = ['b', 'a', 'c']
sorted_characters = sorted(characters)

print(sorted_characters)

