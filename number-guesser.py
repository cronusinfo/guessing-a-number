import random


top_of_range = input("type a number: ") # getting the user input
if top_of_range.isdigit(): #checking if digit
    top_of_range = int(top_of_range) #if its a digit the input will converted to an integer
    if top_of_range <= 0: #checking if the input is higher than zero
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print("Please input a digit next time")
    quit()

randoms = random.randint(0, top_of_range) #if the user put a required digit the random module will be implement here
guesses = 0

#loop the process and it will keep asking a user to guess it
while True:
    # while its true that the user inputs a digit it be counted on a guesses variable
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == randoms: #if the user guess variable as input will be equal to random generated number then it will be print out the correct
            print("You got it correct")
            break
        else:
            print("You got it wrong")
            if user_guess > randoms:
                print("You are above the number")
            else:
                print("You are bellow the number")
    else:
        print("Please input a number")
        continue


print("You got in " +str(guesses)+ " guesses")