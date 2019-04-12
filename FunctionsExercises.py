'''
Created on Jan 24, 2019

@author: darrenbean
'''
def collatz(number):
    if number % 2 == 0:
        print("it's even")
        halfofnumber = int(number/2)
        print(str(number) + " / 2 = " + str(halfofnumber))
        return halfofnumber
        
    if number % 2 ==1:
        print("it's odd")
        changednumber = int(((3 * number) + 1))
        print(str(number) + " * 3 + 1 = " + str(changednumber))
        return changednumber

def getNumber(user_input):
    while True:
        try:
            input_to_check = int(input(user_input))
        except ValueError:
            print("Not an integer! Try again, eh?")
            continue
        else:
            return input_to_check
            break

#this would be "main"
number = getNumber("Enter an integer please:  ")

print("Thank you for entering an integer." \
      " Some people don't know what an integer is. Tragic.")

while number != 1:
    number = collatz(number)  
    
print("That's the end of the sequence.")
    
        
    