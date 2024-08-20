import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0
    max_attempts = 10
    
    print("This is a simple guessing game numbers between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess the number.")
    
    while guess != number_to_guess and attempts < max_attempts:
        try:
            guess = int(input("Take a guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue  
            
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low.")
            elif guess > number_to_guess:
                print("Too high.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts!")
        except ValueError:
            print("Enter a valid number!")
            
        if attempts == max_attempts:
            print(f"Sorry you're out of attempts :( The number was {number_to_guess}")
            
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        guessing_game()
    else:
        print("Thanks for playing :)")
        
            
if __name__ == "__main__":
    guessing_game()

