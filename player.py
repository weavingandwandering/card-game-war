class Player:

    def __init__(self,name):

        self.name = name 
        self.current_cards = []


    def __str__(self):
        return f'Player {self.name} has {len(self.current_cards)} cards.'
    

    def remove_card(self):
        """
        removes and returns the top card from the player's deck
        """
        return self.current_cards.pop(0)

    def add_card(self, new_card):
        """
        adds the new card(s) to the end of the player's deck 
        """
        if type(new_card) == type(list):
            self.current_cards.extend(new_card)
        else:
            self.current_cards.append(new_card)
        
