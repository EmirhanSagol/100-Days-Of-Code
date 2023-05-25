import random
import os 
import Art

def draw_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] # The 10's represent each of the "K, Q, and J". 11 is represent A.
    card = random.choice(cards)
    return card

def calculate(deck):
    """Picks up a deck and checks the score."""
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
        print(f"11 now count as 1. Deck: {deck} ")
    if sum(deck) > 21:
        print(f"Deck: {deck} is over 21.")
    return deck
        
def compare(user_deck, computer_deck):
    """Takes two decks and compares their scores."""
    if sum(user_deck) > 21:
        print("Your deck over 21. You lost.")
    elif sum(computer_deck) > 21:
        print("Oppenent deck over 21. You win.")
    elif sum(user_deck) > sum(computer_deck):
        print(f"Your Score: {sum(user_deck)}\nComputer Score: {sum(computer_deck)}\nYou win.")
    elif sum(computer_deck) > sum(user_deck):
        print(f"Your Score: {sum(user_deck)}\nComputer Score: {sum(computer_deck)}\nYou lost.")
    elif sum(computer_deck) == sum(user_deck):
        print(f"Your Score: {sum(user_deck)}\nComputer Score: {sum(computer_deck)}\nDraw.")

clear = lambda: os.system('cls')

def Blackjack():
    game_start = True
    user_deck = []
    computer_deck = []
    print(Art.logo)
    for i in range(2):
        user_deck.append(draw_card())
        computer_deck.append(draw_card())

    while game_start == True:
        if sum(user_deck) > 21:
            game_start = input("Do you want another Blackjack game. Type 'y' to play, type 'n' to quit\n")
            if game_start == "y":
                game_start == True
                clear()
                Blackjack()
            elif game_start == "n":
                quit()

        answer = input(f"Your deck: {user_deck}\nComputer deck: {computer_deck[0]}\nType 'y' to get another card, type 'n' to pass.\n")
        clear()
        if answer == "y":
            user_deck.append(draw_card())
            user_deck = calculate(user_deck)
        elif answer == "n":
            print(f"Computer deck: {computer_deck}")
            computer_deck = calculate(computer_deck)
            while sum(computer_deck) < 17:
                computer_deck.append(draw_card())
                print(f"Computer deck: {computer_deck}")
                computer_deck = calculate(computer_deck)

            compare(user_deck, computer_deck)
            game_start = input("Do you want another Blackjack game. Type 'y' to play, type 'n' to quit\n")
            if game_start == "y":
                game_start == True
                clear()
                Blackjack()
            elif game_start == "n":
                quit()

Blackjack()
