from deck import Deck
from card import Card
from player import Player


new_deck = Deck()
print(new_deck.add_cards[0])

new_deck.shuffle_deck()
print(new_deck.add_cards[0])

new_player = Player("Ishita")
print(new_player)

sample_card = new_deck.deal_card()
new_player.add_card(sample_card)

print(new_player)