import random  # you have to import a module

n = random.randint(1,10)  # in random we take randint which will have random numbers
guess = 0

while guess != n:
    guess = int(input("Enter a number: "))
    if guess < n:
        print("Too small")
    elif guess > n:
        print("Too large")
    else:
        print("You got it!")