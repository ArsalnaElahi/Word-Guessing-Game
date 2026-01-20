import random

WORDS = {
    "easy": ["tax", "cat", "box", "hello", "pass", "tree"],
    "medium": ["python", "ocean", "planet", "laptop", "india"],
    "hard": ["library", "diamond", "ethical", "mountain", "programming"]
}

MAX_ATTEMPTS = 7


def choose_secret(level):
    return random.choice(WORDS.get(level, WORDS["easy"]))


def generate_hint(secret, guess):
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += secret[i]
        else:
            hint += "_"
    return hint


def play_game():
    print("Welcome to the Password Guessing Game!")
    print("Choose difficulty: easy, medium, hard")

    level = input("Enter difficulty: ").lower()
    secret = choose_secret(level)

    attempts = 0

    print("\nGuess the secret word!")

    while attempts < MAX_ATTEMPTS:
        guess = input("Enter your guess: ").lower()

        if not guess:
            print("Empty input is not allowed.")
            continue

        attempts += 1

        if guess == secret:
            print(f"Correct! You guessed it in {attempts} attempts.")
            return

        hint = generate_hint(secret, guess)
        print(f"Hint: {hint}")
        print(f"Attempts left: {MAX_ATTEMPTS - attempts}")

    print(f"\n❌ Game over! The secret word was: {secret}")


if __name__ == "__main__":
    play_game()
