#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Create non-randomized list
not_randomized = []

# Create completely randomized list
completely_randomized = []

# Get total length of password
total_pass_length = nr_letters + nr_numbers + nr_symbols
print(f"Request length: {total_pass_length}")

# Add count(nr_letters) of random letters to newly created non-randomized list
nl = 0
while nl < nr_letters:
  random_selection = random.choices(letters)
  not_randomized.append(random_selection[0])
  nl += 1
  
# Add count(nr_symbols) of random symbols to newly created non-randomized list
ns = 0
while ns < nr_symbols:
  not_randomized.append(random.choices(symbols)[0])
  ns += 1
  
# Add count(nr_numbers) of random numbers to newly created non-randomized list
nn = 0
while nn < nr_numbers:
  not_randomized.append(random.choices(numbers)[0])
  nn += 1


while (len(not_randomized) != 0):

    print("Not randomized: ", not_randomized)

    randomized_int = random.randint(0, len(not_randomized ) - 1)
    randomized_value = not_randomized[randomized_int]

    completely_randomized.append(randomized_value[0])
    del not_randomized[randomized_int]

    print("Completely Randomized: ", completely_randomized, "\n")

finished_pass = "".join(completely_randomized)

print(finished_pass)