def get_feedback():
    while True:
        feedback = input("Is my guess too high (h), too low (l), or correct (c)? ").strip().lower()
        if feedback in ['h', 'l', 'c']:
            return feedback
        print("Please enter 'h' for too high, 'l' for too low, or 'c' for correct.")

def guessing_game():
    low, high = 1, 100
    guesses = []

    print("Think of a number between 1 and 100, and I will try to guess it.")
    input("Press Enter when ready...")

    while True:
        comp_guess = (low + high) // 2
        guesses.append(comp_guess)
    
        print(f"Computer guesses: {comp_guess}")
    
        feedback = get_feedback()    

        if feedback == 'c':
            print(f"Got it! Your number was {comp_guess}")
            break

        elif feedback == 'l':
            low = comp_guess + 1

        else: # for feedback == 'h'
            high = comp_guess - 1

            guesses.pop()  # Remove invalid guess from list
    
    print(f"Guessed in {len(guesses)} attempts!")


if __name__ == "__main__":
    guessing_game()