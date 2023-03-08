# Helpful resource: https://www.programiz.com/python-programming/examples/prime-number

#Write your code below this line 👇
import math
isTrueMessage = "It's a prime number."
isFalseMessage = "It's not a prime number."

def prime_checker(number):
    #Define a flag variable
    hasFactor = False

    if number == 1:
        print(isFalseMessage)
    elif number >1:
        for i in range (2, number):
            if (number % i) == 0:
                # If factor is found, set to true and break out of loop.
                hasFactor = True
                break
        if hasFactor:
            print(isFalseMessage)
        else:
            print(isTrueMessage)

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
