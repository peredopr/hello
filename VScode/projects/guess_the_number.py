print("Guess the right number (1 to 10), you have 3 tries!")
guess = 0
while guess < 3:
    i = int(input("Guess: "))
    guess += 1
    if i == 9:
        print("Congratulations! You guessed the right number!")
        break
    else:
        print("Wrong number.")
else:
    print("You failed! Try again some other time.")