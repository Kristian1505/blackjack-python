import random

### Display a Welcome Message to the Player ###
def display_welcome_message():
    print("""Welcome to the Blackjack game!
Here, you will have the opportunity to get rich!
Just make sure you win! ;)
Let's get started!
          """)

### Get a Random Card from Deck ###
def get_random_card(deck):
    return deck[random.randint(0, len(deck) - 1)]

### Deal Cards to Each Hand, It Uses the Function get_random_card ###
def deal_cards(number_of_cards, hand, deck, random_card):

    if number_of_cards > 1:
        for n in range(1, number_of_cards + 1):
            hand.append(random_card(deck))
    else:
        hand.append(random_card(deck))
    
    return hand

### Sum of the Card Values in the Hand ###
def calculate_hand_value(hand):
    total = 0
    for n in (hand):
        total += n

    if total > 21 and 11 in hand:
        total -= 10
        hand[hand.index(11)] = 1 #Change Ace from 11 to 1

    return total

    
### Replace the First Card with a "?" to Hide It ###
def hide_card(hand):
    secret_hand = hand.copy()
    secret_hand[0] = "?"
    return secret_hand

### Ask Player for Another Card ###
def take_another_card():
    user_answer = input('Would you like to take another card? Type "y" for yes or "n" for no: ')
    print("\n")
    return user_answer.lower() == "y"


### Ask Player for Playing Again ###
def play_again():
    user_answer = input('Would you like to play again? Type "y" for yes or "n" for no:')
    return user_answer.lower() == "y"

"""
def return_ace(hand):
    counter = 0
    list_with_aces = hand.copy()
    for n in hand:
        if n == 11 or n == 1:
            list_with_aces[counter] = "Ace"

        counter += 1
    
    return list_with_aces
"""

"""
### Sum of the Card Values in the Hand ###
def calculate_hand_value(hand):
    total = 0
    ace_counter = 0
    ace_index_list = []
    ace_list = []

    if "Ace" in hand:
        ace_index = hand.index("Ace")
        hand[ace_index] = 11
        ace_list[ace_counter].append("Ace")
        ace_index_list.append(ace_index)

    for n in (hand):
        total += n

    if total > 21 and 11 in hand:
        total -= 10
        hand[hand.index(11)] = 1 #Change Ace from 11 to 1

    return total
"""