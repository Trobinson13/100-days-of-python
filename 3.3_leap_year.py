# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leap_year = False
is_leap_year = "Leap year."
not_leap_year = "Not leap year."

if (year % 4 == 0):
    leap_year = True

    if (year % 100 == 0):
        leap_year = False

        if(year % 400 == 0):
            leap_year = True

if (leap_year == True):
    print(is_leap_year)

else:
    print(not_leap_year)
