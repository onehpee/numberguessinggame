import random
def game_round(rounds):
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    for num_rounds in range(1, rounds + 1):
        print(f"Round {num_rounds}: Guess the number between 1 and 100")
        random_num = random.randint(1, 100)
        guesses = 0
        
        while True:
            try:
                guess = int(input("Enter your guess: "))
                guesses += 1
                if guess == random_num:
                    print(f"Congratulations! You guessed the correct number in ${guesses} attempts.")
                elif guess < random_num:
                    print(f"Incorrect! The number is less than ${guess}.")
                else:
                    print(f"Incorrect! The number is greater than ${guess}.")
            except ValueError:
                print("Invalid input. Enter a number")
    


    
    print("Round ended.")
    return True  # Or return False to stop the game

def main():
  
if __name__ == "__main__":
    main()




