from functions import get_random_card
from functions import deal_cards
from functions import calculate_hand_value
from functions import display_welcome_message
from functions import hide_card
from functions import take_another_card
from functions import play_again
from functions import restore_values


deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
user_hand =  []
dealer_wins = False
take_card = True
keep_playing = True

### Say Welcome to the Player ###
display_welcome_message()

while keep_playing:

    deal_cards(2, dealer_hand, deck, get_random_card) #Deal initial cards to the dealer
    summatory_dealer = calculate_hand_value(dealer_hand)
    print("\n")
    print(f"The dealer's hand: {hide_card(dealer_hand)}") #Hide first card and print value of second card

    while take_card:
        card_counter = 1
        if len(user_hand) < 2:

            deal_cards(2, user_hand, deck, get_random_card) #Deal initial cards to the user
            print(f"The dealer dealt you the cards {user_hand[0]} and {user_hand[1]}")
            print(f"Your current hand: {user_hand}") #Print values of card
            summatory_user = calculate_hand_value(user_hand)
            print(f"Total points in your hand: {summatory_user} \n")

        
        else:

            card_counter += 1
            deal_cards(1, user_hand, deck, get_random_card) #Deal cards to the user
            summatory_user = calculate_hand_value(user_hand)
            print(f"The dealer dealt you the card {user_hand[card_counter]}")
            if summatory_user > 21:
                break
            print(f"Your current hand: {user_hand}") #Print values of card
            print(f"Total points in your hand: {summatory_user}")

        if summatory_user > 21:
            break

        take_card = take_another_card()


    take_card = True


    while take_card:
        card_counter = 1

        if summatory_user > 21:
            print("Oh no! You've gone over 21. You lose!")
            print(f"Your final hand was: {user_hand} = {summatory_user} points")

            break

        ### Dealer  Takes Cards ###
        while summatory_dealer < 17:
            card_counter += 1
            deal_cards(1, dealer_hand, deck, get_random_card)
            print("The dealer is taking a card")
            print(f"The dealer got the card {dealer_hand[card_counter]}")
            print(f"The dealer's hand: {dealer_hand}")
            print("\n")
            summatory_dealer = calculate_hand_value(dealer_hand)
        
        if summatory_user <= 21 and summatory_user > summatory_dealer:
            print("Congratulations! You win!")
            print(f"Your hand: {user_hand} = {summatory_user} points")
            print(f"The dealer's hand: {dealer_hand} = {summatory_dealer} points")


        elif summatory_dealer == summatory_user:
            print("It's a draw!")
            print(f"Your hand: {user_hand} = {summatory_user} points")
            print(f"The dealer's hand: {dealer_hand} = {summatory_dealer} points")

        elif summatory_dealer > summatory_user and summatory_dealer <= 21:
            print("The dealer wins this round. Better luck next time!")
            print(f"Your hand: {user_hand} = {summatory_user} points")
            print(f"The dealer's hand: {dealer_hand} = {summatory_dealer} points")

        else:
            print("Congratulations! You win!")
            print(f"Your hand: {user_hand} = {summatory_user} points")
            print(f"The dealer's hand: {dealer_hand} = {summatory_dealer} points")

            
        take_card = False
    
    keep_playing = play_again()
    take_card = restore_values(dealer_hand, user_hand)
