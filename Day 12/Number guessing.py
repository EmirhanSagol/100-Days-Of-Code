import random

print("Welcome to do number guessing game! \nI'm thinking of a number between 1 and 100.")
difficult_answer = input("Write a difficulty level of the game. Type 'easy' to easy level or 'hard' to hard level\n")

if difficult_answer == "easy":
    attempt = 10
elif difficult_answer == "hard":
    attempt = 5

answer = random.randint(1, 100)
predicted_number = 0

while attempt > 0:
    if predicted_number == answer:
        quit()
    predicted_number = int(input(f"You have {attempt} attempts remaining to guess the number.\nMake a guess: "))
    if predicted_number > answer:
        print("Too High!")
        attempt -= 1
    elif predicted_number < answer:
        print("Too Low!")
        attempt -= 1
    else:
        print(f"You got it! Answer is {answer}.")

print("You've run out of guesses, you lose.")