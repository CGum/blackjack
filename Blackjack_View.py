import sys
import time

import Blackjack_Controller
import Blackjack_Model

card_design = """\
┌───────────┐
│{}         │
│           │
│           │
│     {}    │
│           │
│           │
│         {}│
└───────────┘
""".format('{val: <2}', '{suit: <2}', '{val: >2}')
# formatting of the card and space values to make the card keep its shape

hidden_card_design = """\
┌───────────┐
│░░░░░░░░░░░│
│~~~~~~~~~~~│
│░░░░░░░░░░░│
│~~~~???~~~~│
│░░░░░░░░░░░│
│~~~~~~~~~~~│
│░░░░░░░░░░░│
└───────────┘
"""  # dealer will hide one of the cards on the initial hand


# the functions join_lines(), hidden_card(), print_hand() and card_design/hidden_card_design were referenced from
# https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
# These functions were changed to work with how I have coded this program, they don't have any part in game logic but
# are only there to make the playing experience a bit better by providing better looking aesthetic elements

def print_hand(hand):  # print a hand using ascii card design
    def card_to_string(*hand):
        name_to_symbol = {  # used for mapping suit name to its corresponding symbol
            'S': '♠', 'D': '♦', 'H': '♥', 'C': '♣',
        }

        for card in hand:  # go through all the cards currently in the hand
            suit, value = card.split(":")  # ex. C:3 gets split to suit = C (clubs) value = 3
            return card_design.format(val=value, suit=name_to_symbol[suit])

    return join_lines(map(card_to_string, hand))


def join_lines(strings):
    # Stack strings horizontally, this doesn't keep lines aligned unless the preceding lines have the same length
    lines = [string.splitlines() for string in strings]
    return '\n'.join(''.join(lines) for lines in zip(*lines))


def hidden_card(hand):  # dealer will hide the card on the right
    return join_lines((print_hand(hand[:1]), hidden_card_design))


def print_final_results(dealer_hand, player_hand):  # print both dealer's and player's hand, and both totals at
    # the very end
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("\t\t  Final Results\n")
    time.sleep(1)
    print(
        "Dealer Hand : \n" + str(print_hand(dealer_hand)) + " \t\tDealer Total : " + str(
            Blackjack_Model.total_value(dealer_hand)))
    print(
        "\nPlayer Hand : \n" + str(print_hand(player_hand)) + " \t\tPlayer Total :  " + str(
            Blackjack_Model.total_value(player_hand)))


def print_bj(num):
    if num == 0:
        print('WOW! You and the Dealer got a blackjack! It is a push!')
    elif num == 1:
        print("\nYou win! You got a Blackjack!\n")
    else:
        return


def all_results(num):  # all the win/lose conditions
    if num == 0:
        print('\nWOW! You and the Dealer got a blackjack! It is a push!\n')
    elif num == 1:
        print("\nYou win! You got a Blackjack!\n")
    elif num == 2:
        print('\nDealer got a blackjack! Dealer wins!\n')
    elif num == 3:
        print("\nYou bust! You lost!\n")
    elif num == 4:
        print("\nDealer bust! You win! \n")
    elif num == 5:
        print("\nDealer has a better hand than you! Dealer wins! \n")
    elif num == 6:
        print("\nYou have a better hand than the dealer! You win!\n")
    elif num == 7:
        print("\nIt's a push! No one wins!\n")
    else:
        return


def print_player_hand(hand):
    print(
        "Player Hand : \n" + str(print_hand(hand)) + " \t\tPlayer Hand Total : " + str(
            Blackjack_Model.total_value(hand)))


def print_dealer_initial(hand):  # used to print initial dealer hand with 1 card hidden
    print("Dealer Hand : \n" + str(hidden_card(hand)))


def print_dealer_hand(hand):
    print(
        "Dealer Hand : \n" + str(print_hand(hand)) + " \t\tDealer Hand Total : " + str(
            Blackjack_Model.total_value(hand)))


def print_dealerhit():
    print("\nDealer Hits!\n")


def welcome_msg():
    print("""    
        .-. .-')              ('-.             .-. .-')             ('-.             .-. .-')        .-. .-')              
    \  ( OO )            ( OO ).-.         \  ( OO )           ( OO ).-.         \  ( OO )       \  ( OO )             
     ;-----.\ ,--.       / . --. /  .-----.,--. ,--.     ,--.  / . --. /  .-----.,--. ,--.        ;-----.\  ,--.   ,--.
     | .-.  | |  |.-')   | \-.  \  '  .--./|  .'   / .-')| ,|  | \-.  \  '  .--./|  .'   /        | .-.  |   \  `.'  / 
     | '-' /_)|  | OO ).-'-'  |  | |  |('-.|      /,( OO |(_|.-'-'  |  | |  |('-.|      /,        | '-' /_).-')     /  
     | .-. `. |  |`-' | \| |_.'  |/_) |OO  )     ' _) `-'|  | \| |_.'  |/_) |OO  )     ' _)       | .-. `.(OO  \   /   
     | |  \  (|  '---.'  |  .-.  |||  |`-'||  .   \ ,--. |  |  |  .-.  |||  |`-'||  .   \         | |  \  ||   /  /\_  
     | '--'  /|      |   |  | |  (_'  '--'\|  |\   \|  '-'  /  |  | |  (_'  '--'\|  |\   \        | '--'  /`-./  /.__) 
     `------' `------'   `--' `--'  `-----'`--' '--' `-----'   `--' `--'  `-----'`--' '--'        `------'   `--'      
                 ('-.  _   .-')                                                                                        
               _(  OO)( '.( OO )_                                                                                      
       .-----.(,------.,--.   ,--.)        ,----.                                                                      
      '  .--./ |  .---'|   `.'   |        '  .-./-')                                                                   
      |  |('-. |  |    |         |        |  |_( O- )                                                                  
     /_) |OO  ||  '--. |  |'.'|  |        |  | .--, \                                                                  
     ||  |`-'| |  .--' |  |   |  |       (|  | '. (_/                                                                  
    (_'  '--'\ |  `---.|  |   |  |        |  '--'  |                                                                   
       `-----' `------'`--'   `--'         `------'                                                                    

    """)


def goodbye_msg():
    print("""   

        ____   U  ___ u  U  ___ u ____   ____  __   _U _____ u 
    U /"___|u  \/"_ \/   \/"_ \/|  _"U | __")u\ \ / \| ___"|/ 
    \| |  _ /  | | | |   | | | /| | | \|  _ \/ \ V / |  _|"   
     | |_| .-,_| |_| .-,_| |_| U| |_| || |_) |U_|"|_u| |___   
      \____|\_)-\___/ \_)-\___/ |____/ |____/   |_|  |_____|  
      _)(|_      \\        \\    |||_ _|| \\.-,//|(_ <<   >>  
     (__)__)    (__)      (__)  (__)_(__) (__\_) (__(__) (__) 

    """)


def input_play_again():
    user_input = input("Do you want to play again? (Y or N) : ").lower()
    if user_input == "y":
        Blackjack_Controller.start_game()
    elif user_input == 'n':
        goodbye_msg()
        sys.exit()
    else:
        print('Please either choose Y or N')
        input_play_again()


def input_hit_stand():
    user_input = input("Do you want to Hit or Stand (H or S) : ").lower()
    return user_input


def print_error_handling():
    print('Please either choose Hit (H) or Stand (S)')
