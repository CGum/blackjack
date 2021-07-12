import random

deck = []


def make_deck():
    global deck
    deck[:] = []  # empty the list to not get duplicates (this is only a problem when playing again/making new deck)
    # with the colons after the letters, it makes splitting the string correctly easy
    suits = ['H:', 'D:', 'S:', 'C:']  # hearts, diamonds, spades, clubs
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'J', 'Q']

    for suit in suits:
        for value in values:
            deck.append(suit + value)  # H2 D6 S10 CJ etc. deck is made with 52 cards
    random.shuffle(deck)


def deal(deck):
    hand = []
    for i in range(2):  # loop  twice to give 2 cards to dealer's or player's  hand
        card = deck.pop()  # pop element from list
        hand.append(card)  # add element to player's or dealer's hand
    return hand


def hit(hand):
    card = deck.pop()  # pop an element from the deck
    hand.append(card)  # add element to hand
    return hand


def total_value(hand):
    tot = 0
    contain_ace = False

    for card in hand:  # go through all the cards currently in the hand
        suit, value = card.split(":")  # ex. C:3 gets split to suit = C (clubs) value = 3
        if value == 'K' or value == 'J' or value == 'Q':  # king jack queen are worth 10
            tot += 10
        elif value == 'A':  # total goes up by 11 or 1 from Ace depending on the current total
            contain_ace = True
            tot += 11
        else:  # if the card isn't queen king joker ace, just add its normal value to the total
            tot += int(value)

    # we want the value of ace to go from 11 to 1 if the total value of the hand is over 21
    if contain_ace and tot > 21:
        tot -= 10

    return tot


def win_cond_bj(dealer_hand, player_hand):  # check the win condition -> is player getting blackjack
    # even if the dealer gets 21, don't just end game and let the player play and have a chance to get a push

    if total_value(player_hand) == 21 and total_value(dealer_hand) == 21:
        return 0
    elif total_value(player_hand) == 21 and total_value(dealer_hand) != 21:
        return 1
    else:
        return


def all_win_cond(dealer_hand, player_hand):
    if total_value(player_hand) == 21 and total_value(dealer_hand) == 21:
        return 0
    elif total_value(player_hand) == 21 and total_value(dealer_hand) != 21:
        return 1
    elif total_value(dealer_hand) == 21:
        return 2
    elif total_value(player_hand) > 21:
        return 3
    elif total_value(dealer_hand) > 21:
        return 4
    elif total_value(player_hand) < total_value(dealer_hand):
        return 5
    elif total_value(player_hand) > total_value(dealer_hand):
        return 6
    elif total_value(player_hand) == total_value(dealer_hand):
        return 7
    else:
        return

