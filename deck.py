from random import shuffle 
from card import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
                'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Deck:

    def __init__(self):
        self.add_cards = []
        for suit in suits:
            for rank in ranks:

                created_card = Card(suit, rank)

                self.add_cards.append(created_card)


    def shuffle_deck(self):

        shuffle(self.add_cards)


    def deal_card(self):
        
        return self.add_cards.pop()
    
    