
from player import Player
from deck import Deck
#game setup

player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

#splitting the 52 cards 
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())



#while game_on
game_on = True

round_num = 0

while game_on:

    round_num +=1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print('Player one, out of cards! Player Two Wins!')
        game_on = False
        break
    if len(player_two.all_cards) ==0:
        print('Player two out of cards! Player one Wins!')
        game_on =False
        break

    #start a new round
    #this is the current card on play
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards =[]
    player_two_cards.append(player_two.remove_one())

# we have 3 situation
    #player one > player two
    #player one < player two
    #player one == player two
# addition rules draw 5 cards and player loese if they dont have at least 5 cards to play the war
    
    at_war = True

    #while at_war

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False
        
        else:
            print('WAR !')

            if len(player_one.all_cards) < 5:
                print('player one unable to declare war')
                print('player two wins')
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print('player two unable to declare war')
                print('player one wins')
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
