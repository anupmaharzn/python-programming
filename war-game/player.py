# player class

    # this class will be used to hold a player's current list of cards.
    # a player should be able to add or remove cards from their 'hand'(list of card objects)
    # we will want the player to be able to add a single card or multiple cards to their list

    #we need to think about is translating a deck/hand of card with top and bottom

    #pop from 0
    #append simple means right aka bottom or use extend() fro mutliple cards (extend merges the list) why no append coz it nest the list




from deck import Deck


class Player():

    def __init__(self,name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        #list of multiple card objects
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            #for single card object
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards.'
    


# new_player = Player('anup')

# print(new_player)

# new_dek = Deck()

# my_card = new_dek.deal_one()

# print(my_card)


# new_player.add_cards(my_card)

# print(new_player)
# print(new_player.all_cards[0])

# new_player.add_cards([my_card,my_card,my_card])

# print(new_player)

# new_player.remove_one()

# print(new_player)

# print(new_player.all_cards[0].rank)