import random

# Generate a random number between 1 and 9
n = random.randrange(1, 10)

# Initialize guess to None to enter the loop
guess = None

# Explain the game to the user
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

while n != guess:
    try:
        # Take a guess from the user
        guess = int(input("Enter your guess: "))
        
        # Check if the guess is too low
        if guess < n:
            print("Too low! Try again.")
        
        # Check if the guess is too high
        elif guess > n:
            print("Too high! Try again.")
        
        # Correct guess, break out of the loop
        else:
            break
    
    # Handle invalid input
    except ValueError:
        print("Please enter a valid number.")

# Congratulate the user
print("Congrats, you guessed the right number!")





