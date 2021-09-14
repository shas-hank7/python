""" name = input("Enter the name of recipient\n")
date = input("Enter Date\n")

print("Dear " + name + "\nYou are selected!\n"+date)
"""

#or

letter='''Dear <name>
You are selected!
 
Date: <date>'''

name = input("Enter the name of recipient\n")
date = input("Enter Date\n")

letter=letter.replace("<name>", name)
letter=letter.replace("<date>", date)
print(letter)