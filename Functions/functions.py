def multiply(x, y):
    return x*y


def isPalindrome(string):
    return string[::-1].casefold() == string.casefold()


def isPalindromeSentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string+=char
    # print("Hello")
    return isPalindrome(string)


def fibonacci(n):
    """
    Returns the `n`th Fibonacci number for positive `n`.
    """
    result = None
    if 0<=n <= 1:
        return n
    numberBefore, numberBeforeBefore = 1, 0
    for i in range(n-1):
        result = numberBefore + numberBeforeBefore
        numberBeforeBefore = numberBefore
        numberBefore = result
    return result

for i in range(36):
    print(i, fibonacci(i))