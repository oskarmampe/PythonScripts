import random

print("----------------------------------")
print("     GUESS THAT NUMBER GAME       ")
print("----------------------------------")

the_number = random.randint(0, 100)

while True: 
    guess_text = input("Guess a number between 0 and 100: ")
    guess = int(guess_text)
    if the_number > guess:
        print("Your guess of {0} was too LOW.".format(guess))
    elif the_number < guess:
        print("Your guess of {0} was too HIGH.".format(guess)) 
    else:
        print("Congratulations! You won!")
        break  
