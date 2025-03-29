import random
def game_round(rounds):
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
   
    number = random.randint(1, 100)
    guess = 0
    attempts = 0
    print(f"\nRound {rounds}: Guess the number between 1 and 100")

    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print(f"Incorrect! The number is less than {guess}.")
            elif guess > number:
                print(f"Incorrect! The number is greater than {guess}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")

def play_game():
    while True:
        try:
            num_rounds = int(input("How many rounds do you want to play? "))
            if num_rounds <= 0:
                print("Please enter a positive number of rounds.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    for i in range(1, num_rounds + 1):
        game_round(i)
    print("Game over!")

play_game()