import random

play_again = "yes"

while play_again.lower() == "yes":
    secret_number = random.randint(1, 5)
    guess = int(input("Guess the secret number (between 1 and 5): "))

    match guess:
        case _ if guess == secret_number:
            print("Congratulations, you guessed right!")
        case _ if guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")
        case _ if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")
    
    play_again = input("Would you like to play again? (yes/no): ")

print("Thank you for playing. See you later!")