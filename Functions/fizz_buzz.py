def fizz_buzz(n:int) -> str:
    
    
    if n%3==0 or n%5==0:
        if n%3==0 and n%5==0:
            return "fizz buzz"
        if n%3==0:
            return "fizz"
        else:
            return "buzz"
    else:
        return str(n)
        

for i in range(1, 101, 2):
    print(fizz_buzz(i))
    userInput = input()
    rightAnswer = fizz_buzz(i+1)
    if userInput != rightAnswer:
        print("You made a mistake there!")
        break
