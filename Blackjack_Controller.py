import time
import Blackjack_Model
import Blackjack_View

# A 1 player (user vs AI) blackjack game that is made to be played on the terminal


def start_game():
    Blackjack_Model.make_deck()  # make a new deck every time

    dealer_hand = Blackjack_Model.deal(Blackjack_Model.deck)
    player_hand = Blackjack_Model.deal(Blackjack_Model.deck)

    Blackjack_View.print_dealer_initial(dealer_hand)  # show only one card for dealer
    Blackjack_View.print_player_hand(player_hand)  # print player hand and the total value of the hand
    check_blackjack(dealer_hand, player_hand)  # check for blackjack after 2 cards

    while 1:
        user_input = Blackjack_View.input_hit_stand()
        if user_input == 'h':  # while hitting, player will either get blackjack or go over 21 and bust

            Blackjack_Model.hit(player_hand)
            time.sleep(.2)

            check_blackjack(dealer_hand, player_hand)
            Blackjack_View.print_player_hand(player_hand)

            if Blackjack_Model.total_value(player_hand) > 21:
                check_all_results(dealer_hand, player_hand)

        elif user_input == 's':  # while player stands, dealer hits until at least 17

            while Blackjack_Model.total_value(dealer_hand) < 17:
                # dealer will get either 17 to 21 or blackjack or bust
                Blackjack_Model.hit(dealer_hand)
                Blackjack_View.print_dealerhit()
                time.sleep(1)
                Blackjack_View.print_dealer_hand(dealer_hand)
                check_blackjack(dealer_hand, player_hand)

                if Blackjack_Model.total_value(dealer_hand) > 21:
                    check_all_results(dealer_hand, player_hand)
            check_all_results(dealer_hand, player_hand)

        else:
            Blackjack_View.print_error_handling()


def check_blackjack(dealer_hand, player_hand):
    # simple controller method that uses model to check for blackjack, updates view if so
    bj = Blackjack_Model.win_cond_bj(dealer_hand,
                                     player_hand)  # check if player got a blackjack (21) after 2 cards

    if bj == 0 or bj == 1:
        time.sleep(1)
        Blackjack_View.print_final_results(dealer_hand, player_hand)
        Blackjack_View.print_bj(bj)
        Blackjack_View.input_play_again()


def check_all_results(dealer_hand, player_hand):
    # another simple controller method that uses model to check all results and updates view
    wincond = Blackjack_Model.all_win_cond(dealer_hand, player_hand)
    if wincond == 0 or wincond == 1 or wincond == 2 or wincond == 3 or wincond == 4 or wincond == 5 or wincond == 6 \
            or wincond == 7:
        Blackjack_View.print_final_results(dealer_hand, player_hand)
        Blackjack_View.all_results(wincond)
        Blackjack_View.input_play_again()


def main():
    Blackjack_View.welcome_msg()
    time.sleep(2)
    start_game()


if __name__ == "__main__":
    main()
