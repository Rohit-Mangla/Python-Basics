import random
num = 1
print("welcome to the number guessing game.we have a number to be guessed.you have 5 attempts")
print("The secret number is between 1 and 100")
secret_number = random.randint(1,100)
attempts = 5
is_guess_correct = False

while num <= 5:
    print(f"you have {attempts} attempts remaining.")
    user_number = int(input("Enter your guess: "))
    if user_number == secret_number:
        print("congrats! your guess is correct!")
        is_guess_correct = True
        break
    else:
        if user_number < secret_number:
            higher_or_lower = "higher"
        else:
            higher_or_lower = "lower"
        print(f"your guess is wrong! Try {higher_or_lower} number.")

    num = num + 1
    attempts = attempts - 1

if not is_guess_correct:
    print("Bad luck! You exhausted all your attempts and couldn't guess the number.")
print(f"The secret number is {secret_number}.Game over")
