#print("Hello World")

import random

# For lab evaluation and passing the test cases, secret number is set to 42.
# Change to False to play with live random generation.
TEST_MODE = True


def get_secret_number() -> int:
    
    if TEST_MODE:
        return 42
    return random.randint(1, 100)


def get_valid_guess(attempts_left: int) -> int:
    
    while True:
        raw_val = input("Enter your guess: ").strip()

        # Step 1: Whole number verification
        try:
            val = int(raw_val)
        except ValueError:
            print("Invalid input. Enter a whole number.")
            print(f"Attempts left: {attempts_left} (no attempt lost)")
            continue

        # Step 2: Range verification (1 to 100)
        if val < 1 or val > 100:
            print("Out of range. Enter a number between 1 and 100.")
            print(f"Attempts left: {attempts_left} (no attempt lost)")
            continue

        return val


def play_game():
    
    secret = get_secret_number()
    max_attempts = 5
    attempts_used = 0

    while attempts_used < max_attempts:
        attempts_left = max_attempts - attempts_used
        guess = get_valid_guess(attempts_left)
        attempts_used += 1
        remaining = max_attempts - attempts_used

        if guess == secret:
            attempt_text = "attempt" if attempts_used == 1 else "attempts"
            print(f"Congratulations! You guessed it in {attempts_used} {attempt_text}.")
            return
        elif guess < secret:
            if remaining > 0:
                print(f"Too low! Attempts left: {remaining}")
            else:
                print("Too low")
        else:
            if remaining > 0:
                print(f"Too high! Attempts left: {remaining}")
            else:
                print("Too high")

    print(f"Game Over! The number was {secret}.")


def main():
    
    while True:
        play_game()
        choice = input("Play again? (y/n): ").strip().lower()
        if choice != "y":
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()