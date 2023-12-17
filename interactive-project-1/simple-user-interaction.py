"""
the program will
    display a list
    have a user choose an index position and an input value
    replace value at index position with user's choosen input value

"""

# dis_list = ['1','2','3']
# user_index = None
# user_value = None

# def display(a_list):

#     print(a_list)

# display(dis_list)

# def user_value():

#     index_choice = input('choose index position from 0 or 1 or 2:')
#     value_choice = input ('value you want to write:')
#     return int(index_choice),value_choice

# user_index,user_value = user_value()

# def change_list():
#     dis_list[user_index] = user_value
#     display(dis_list)

# change_list()


game_list = [0,1,2]
game_on = True

def display_game(game_list):
    print('here is the current list')
    print(game_list)


def position_choice():

    choice = 'wrong'

    while choice not in ['0','1','2']:

        choice = input('pick a position (0,1,2):')

        if choice not in ['0','1','2']:
            print('sorry invalid choice!')
        
    
    return int(choice)


def replacement_choice(game_list,position):

    user_placement = input('type a string to place at position:')

    game_list[position] = user_placement

    return game_list




def gameon_choice():

    choice='wrong'

    while choice not in ['Y','N']:

        choice = input('keep playing? (Y or N)')

        if choice not in ['Y','N']:
            print('sorry, i dont understan, please choose Y or N')

        if choice == 'Y':
            return True
        
        else:
            return False
        
while game_on:

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list,position)

    display_game(game_list)

    game_on = gameon_choice()