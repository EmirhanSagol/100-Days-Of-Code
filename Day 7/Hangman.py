import random
import Hangman_Art
import Hangman_Words

list_of_word_letter = []
correct_letters = []
used_letters = []
life = 6
end_of_game = False

print(Hangman_Art.logo)

# Word choosing
word = random.choice(Hangman_Words.word_list)

# Letters of the word are added to the list
for i in word:
    list_of_word_letter.append(i)
    correct_letters.append("_")

copy = list_of_word_letter.copy()

while not end_of_game:
    guess = input("Guess a letter: ")

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in used_letters:
        print(f"You've already guessed {guess}")
    
    # Check guessed letter 
    elif list_of_word_letter.count(guess) > 0:
        for i in range(0, len(list_of_word_letter)):
            if guess == list_of_word_letter[i]:
                correct_letters[i] = guess 
                copy.remove(guess)
                if len(copy) <= 0:
                    print(f"You win!\nAnswer is: {word}")
                    end_of_game = True

    # Wrong answer
    else:
        life -= 1
        print(f"You guessed {guess}, that's not in the word, you lose a life")
        if life == 0:
            print(f"Game over! You Lost\nCorrect answer is {word}")
            end_of_game = True

    used_letters.append(guess)
    print(f"Used letters: {used_letters}\n{''.join(correct_letters)}\n{Hangman_Art.stages[life]}")
