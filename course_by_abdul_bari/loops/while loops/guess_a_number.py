import random

n = random.randint(1,10)
guess = 0

while guess != n:
    guess = int(input("Enter a number: "))
    if guess < n:
        print("Too small")
    elif guess > n:
        print("Too large")
    else:
        print("You got it!")