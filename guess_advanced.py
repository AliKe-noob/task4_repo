import random
from datetime import datetime
STATS_FILE = 'stats.txt'

def save_stats(attempts, difficulty):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(STATS_FILE, "a") as f:
        f.write(f"{timestamp} | {difficulty} | {attempts if attempts is not None else 'Lost'} попыток\n")

# Difficulties chain
def difficulties():
    print("Choose your difficulty: ")
    print("Easy: 1-10, 5 attempts.")
    print("Medium: 1-100, 7 attempts.")
    print("Hard: 1-1000, 10 attempts.")
    
    while True:
        choice = input("Your choice (E, M or H): ")
        
        if choice == "E":
            return 1, 10, 5, "Easy"
        elif choice == "M":
            return 1, 100, 7, "Medium"
        elif choice == "H":
            return 1, 1000, 10, "Hard"
        else:
            print("Nope, type E (Easy), M (Medium) or H (Hard).")

def gameplay(min_num, max_num, max_attempts, difficulty):
    right_number = random.randint(min_num, max_num)
    print(f"Guess the secret number in {difficulty} mode between {min_num} and {max_num}. You have {max_attempts} attempts. ")

    for attempt in range (0, max_attempts + 1):
        while True:
            try:
                guess = int(input(f"Attempts done: {attempt}.   Your guess? "))
                if guess < min_num or guess > max_num:
                    print (f"Please enter a number between {min_num} and {max_num}.")
                    continue
                break
            except ValueError:
                print("Enter a number.")
        
        if guess < right_number:
            print("Try guessing higher.")
        elif guess > right_number:
            print("Try guessing lower.")
        else:
            print(f"Nice, you have guessed the number {right_number} in {attempt} attempts")
            return attempt
    else:
        print(f"Oops, you have used all {max_attempts} attempts. The right number was {right_number}. ")
        return None


def main():
    games = wins = losses = total_attempts = 0
    best = None
    
    while True:
        min_num, max_num, max_attempts, difficulty = difficulties()
        games += 1
        attempts_used = gameplay(min_num, max_num, max_attempts, difficulty)

        if attempts_used is not None:
            wins += 1
            total_attempts += attempts_used
            if best is None or attempts_used < best:
                best = attempts_used
                print(f"New best result: {best} attempt(s).")
            else:
                print(f"Best attempt for this session: {best} attempt(s).")
        else:
            losses += 1

        save_stats(attempts_used, difficulty)

        avg_attempts = total_attempts / wins if wins > 0 else 0
        print(f"Statistics: Total games: {games}, Wins: {wins}, Losses: {losses}, Win rate: {wins/games*100:.2f}%, Average attempts (wins only): {avg_attempts:.2f}")

        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Bye!")
            break

if __name__ == "__main__":
    main()