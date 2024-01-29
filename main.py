from deck import Deck
from card import Card
from player import Player
from random import shuffle
import sys


new_deck = Deck()
print(new_deck.add_cards[0])

new_deck.shuffle_deck()
print(new_deck.add_cards[0])

new_player = Player("Ishita")
print(new_player)

sample_card = new_deck.deal_card()
new_player.add_card(sample_card)

print(new_player)



def game_start():
    
    print("Welcome to War!")
    player_o = input("Player 1, Please enter your name: ")
    player_t = input("Player 2, Please enter your name: ")

    player_one = Player(player_o)
    player_two = Player(player_t)

    new_deck = Deck()
    new_deck.shuffle_deck()
    player_one.add_card(new_deck.add_cards[0:26])
    player_two.add_card(new_deck.add_cards[26:])

    print(player_one)
    print(player_two)

    game_on = True

    while game_on:
        one_war = [] 
        two_war = []
        card_one = player_one.remove_card()
        card_two = player_two.remove_card()

    
        
        print(card_one)
        print(card_two)

        if card_one.value > card_two.value:
            player_one.add_card(card_one)
            player_one.add_card(card_two)
            print("Round won by Player 1!")

            if len(player_two.current_cards) == 0:
                print("Game Won by Player 1!")
                sys.exit()


        elif card_one.value < card_two.value:
            player_two.add_card(card_one)
            player_two.add_card(card_two)
            print("Round won by Player 2!")

            if len(player_one.current_cards) == 0:
                print("Game Won by Player 2!")
                sys.exit()

        else:
            print("The value is the same, the players are going to war!")
            war_on = True
   
            while war_on:
                one_war = player_one.war_card(one_war)
                two_war = player_two.war_card(two_war)
                shuffle(one_war)
                shuffle(two_war)
                one_curr = one_war[0]
                two_curr = two_war[0]

                if one_curr > two_curr:
                    player_one.add_card(one_war)
                    player_one.add_card(two_war)
                    war_on = False
                elif two_curr > one_curr:
                    player_two.add_card(one_war)
                    player_two.add_card(two_war)
                    war_on = False
                else:
                    pass












game_start()

