import random
def play_number_guess():
    while True:
        number = random.randint(1, 10)
        attempts = 0
        max_attempts = 5

        while attempts < max_attempts:
            try:
                guess = int(input("Enter a guess (1-10): "))
            except ValueError:
                print("Enter a valid number!")
                continue

            attempts += 1

            if guess == number:
                print("Correct!")
                break
            elif guess > number:
                print("Too high")
            else:
                print("Too low")

        else:
            print(f"Game Over 😢. The number was {number}.")

        choice = input("Play again? (yes/no): ").strip().lower()
        if choice not in ("yes", "y"):
            print("Thanks for playing.")
            break

if __name__ == "__main__":
    play_number_guess()