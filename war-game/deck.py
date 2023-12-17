#deck class

    #instantiate a new deck
        #create all 52 card objects
        #hold as a list of card objects
    #shuffle a deck through a method call
        #random library shuffle() function
    #deal cards from the deck object
        #pop method from cards list

    #deck class will return card class object instances, not just normal python data types

from card import Card
import random

suits = ('Hearts','Diamonds','Spades','Clubs')

ranks =  ( 
   'Two',
   'Three',
   'Four',
   'Five',
   'Six',
   'Seven',
   'Eight',
   'Nine',
   'Ten',
   'Jack',
   'Queen',
   'King',
   'Ace'
)


class Deck():

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #create the card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):

        random.shuffle(self.all_cards)
    
    def deal_one(self):

        return self.all_cards.pop()


# new_deck = Deck()

# print(new_deck.all_cards[-1])

# new_deck.shuffle()

# print(new_deck.all_cards[-1])

# mycard = new_deck.deal_one()

# print(mycard)

# print(len(new_deck.all_cards))