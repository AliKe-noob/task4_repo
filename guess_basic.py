import random

secret = random.randint(1, 100)
print("I'm thinking of a number between 1-100")

while True:
    guess = int(input("Your guess: "))
    
    if guess < 1 or guess > 100:
        print("Out of range!")
        continue
        
    if guess < secret:
        print("Too low! Try higher")
    elif guess > secret:
        print("Too high! Try lower")
    else:
        print(f"Correct! The number was {secret}")
        break
