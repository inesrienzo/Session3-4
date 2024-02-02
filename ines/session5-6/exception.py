name = input("What is your name?")
age = input("How old are you?")
# print("Hello,", name, "!", sep="")

try:
    age = int(age)  # convert string to integer
    birth_year = 2023 - age
    print(name, ", You were born in", birth_year, ".", sep="")
    number = input("give me a number to divide thed age")
    number = int(number)
    print(age/number)

except ValueError:
        print("hello,", name, "!", sep="")
        print("Invalid age. Please enter a number.")
except ZeroDivisionError:
        print("You cannot divide by zero.")
else:
        print("No exceptions were raised.")
finally:
        print('thank you for playing')

try:
    name = input("What is your name?")
    age = input("How old are you?")
    age = int(age) #convert string to integer
except ValueError:
    print("Invalid age. Please enter a number.")
else:
    if age < 0 or age > 140
    drinks = ("vodka", "tequila", "gin")
    elif age > 120:
        print("You are too old to play the awesome drinking game.")
    elif age < 18:
        print("You are a minor. You can not play the awesome drinking game.")
    elif (country == "USA" or country == "UAE") and age < 21
        print( )
    else:
        print("You are an adult. You can play the awesome drinking game.")
        print("Have some", random.choice(drinks), "and enjoy the game."
import random
# play a dice game with 3 lives, 6 wins the game

lives = 3
while lives > 0:
        print("You have", lives, "Lives left.")
        # roll the dice
        dice = random.randint(1, 6)
        print("You rolled a", dice)
        # check if you win
        if dice == 6:
            print("\n\n YOU WIN!\n\n")
            break
        else:
            lives = lives - 1
    # shorter way do write this: lives -= 1
else:
    print("\n\nYOU LOSE!\n\n")

print("Thank you for playing. Goodbye.")
