import random

top_of_range = input("Type the higest range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
else:
    print("please type a number that is greater than  zero")
    quit()

random_number = random.randint(0,top_of_range)
gusses = 0

while True:
    gusses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please typa a number next time")
        continue
    if user_guess == random_number:
        print("you got it!")
        break
    elif user_guess > random_number :
        print("You were above hit number!")
    else:
        print("you were below the number!")

print("you got it in" , gusses ,"guesses")
