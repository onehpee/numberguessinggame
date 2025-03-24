import random
def play_round():
    random_num = random.choice(100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.")

    response = input("Please select the difficulty level:")
    game_difficulty = response == ""
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    print("Round ended.")
    return True  # Or return False to stop the game

def main():
    play_again = True
    while play_again:
        if not play_round():
            break # Exit loop if play round returns False
        
        response = input("Play another round? (yes/no): ").lower()
        play_again = response == "yes"

    print("Game over.")

if __name__ == "__main__":
    main()




