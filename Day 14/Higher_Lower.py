import GameData
import random
import os
import Art

def compare_followers(data_A, data_B):
    """Compares follower counts. Returns the one with the most followers"""
    if data_A >= data_B:
        return 'A'
    else:
        return 'B'
    
clear = lambda: os.system('cls')
score = 0
game_over = False
rand_data_A = random.choice(GameData.data)

clear()
while not game_over:
    rand_data_B = random.choice(GameData.data)

    # If the data is the same, it will randomly pull the second data again
    while rand_data_A == rand_data_B:
        rand_data_B = random.choice(GameData.data)

    print(Art.logo)
    print(f"Compare A: {rand_data_A['name']}, {rand_data_A['country']}, {rand_data_A['description']}")
    print(Art.vs)
    print(f"Aganist B: {rand_data_B['name']}, {rand_data_B['country']}, {rand_data_B['description']}")
    answer = input("Who has more followers. Type 'A' or 'B': ")

    if answer == compare_followers(rand_data_A['follower_count'], rand_data_B['follower_count']):
        score += 1
        print(f"You're right! Current score: {score}")
        rand_data_A = rand_data_B
        clear()
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True