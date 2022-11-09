from art import logo
from random import randint

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
is_guessed = False

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
print(f"You have {attempts} attempts remaining to guess the number.")

guessed_number = randint(1, 100)
print(guessed_number)
while not is_guessed:
    guess = int(input("Make a guess: "))
    if guess == guessed_number:
        is_guessed = True
        print(f"You got it! The answer was {guessed_number}")
    elif guess != guessed_number:
        if guess > guessed_number:
            print("Too high.")
        elif guess < guessed_number:
            print("Too low.")
        attempts -= 1
        if attempts == 0:
            is_guessed = True
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")











