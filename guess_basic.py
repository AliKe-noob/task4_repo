import random

def generate_secret_number():
    """
    Generates and returns random number 1 - 100.
    """
    return random.randint(1, 100)

def get_user_guess():
    """
    Prompts user to input a guess and handle invalids.

    Returns the int for user guessed number.
    """
    while True:
        try:
            guess = int(input("Your guess: "))
            return guess # Returns the valid input
        except ValueError:
            print("Out of range! Enter a valid Integer.")
        
def provide_feedback(guess, secret):
    """
    Provide feedback based on user's guess.

    Argumenta: 
        guess for int and guessed number of user.
        secret for int and to guess.
    """
    if guess < secret:
        print("Too low! Try higher")
    elif guess > secret:
        print("Too high! Try lower")
    else:
        print(f"Correct! The number was {secret}")


def guess_number():
    """
    main func to the game.
    """
    secret = generate_secret_number()
    print("Im thinking of a number between 1 to 100.")
    
    while True:
        guess = get_user_guess()
        if guess == secret:
            print (f"Correct! The number was {secret}.")
            break
        else:
            provide_feedback(guess, secret)

if __name__ == "__main__":
    guess_number()