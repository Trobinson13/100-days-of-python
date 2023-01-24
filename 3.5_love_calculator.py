# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true_count = 0
true_t_count = 0
true_r_count = 0
true_u_count = 0
true_e_count = 0

love_count = 0
love_l_count = 0
love_o_count = 0
love_v_count = 0
love_e_count = 0

combined_names = (name1 + name2).lower()

for letter in combined_names:
    if (letter == "t"):
        true_t_count += 1
        true_count += 1
    if (letter == "r"):
        true_r_count += 1
        true_count += 1
    if (letter == "u"):
        true_u_count += 1
        true_count += 1
    if (letter == "e"):
        true_e_count += 1
        true_count += 1


    if (letter == "l"):
        love_l_count += 1
        love_count += 1
    if (letter == "o"):
        love_o_count += 1
        love_count += 1
    if (letter == "v"):
        love_v_count += 1
        love_count += 1
    if (letter == "e"):
        love_e_count += 1
        love_count += 1

true_love_value = f"{true_count}" + f"{love_count}"

if (int(true_love_value) < 10 or int(true_love_value) > 90):
    print(f"Your score is {true_love_value}, you go together like coke and mentos.")
elif (int(true_love_value) >= 40 and int(true_love_value) <= 50):
    print(f"Your score is {true_love_value}, you are alright together.")
else:
    print(f"Your score is {true_love_value}.")
