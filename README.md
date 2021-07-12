This is the game Blackjack implemented by using Python.

This is meant to be a game played on the terminal. It is a 1 vs AI game where a user will play against the dealer, where the dealer will play the game by the classic Blackjack rules. To play the game you will have to run the Blackjack_Controller.py file. 

Game Rules:
• The game starts with a standard set of 52 cards randomly shuffled. The value of each card is its associated number with the jack, queen, and king all being worth 10. The ace has the value of 11 unless it is in a hand with a value over 21 in which case it has the value of 1. For example, a hand with an ace and a seven has a value of 18 whereas a hand with an ace, seven, and five has a value of 13. 

• Both the player and the dealer are given 2 cards. The player can see both of their cards but only one of the dealers cards.
• The player now has two option: (1) ”hit” where they are given another card, or (2) ”stand” where they keep the cards they currently have. The player can hit as many times as they wish until they stand. If at any point their hand goes over 21, they automatically lose.

• Once the player has chosen stand and has a hand less then 21, the dealer reveals the other card to
the player. If the value of the dealers hand is 17 or more they automatically stand otherwise they
automatically keep taking more cards until it is at least 17. The dealers decisions are always automatic
whereas the player can choose to hit or stand.

• If the dealers hand goes over 21 the player wins. If the dealers hand is between 17 and 21 (inclusive) then the winner is whoever has the bigger hand.

![p](https://user-images.githubusercontent.com/35476666/125219827-65fe8a80-e27a-11eb-860b-249817e5f0b2.PNG)
![p2](https://user-images.githubusercontent.com/35476666/125219917-a100be00-e27a-11eb-84fd-9f97e37cbbee.PNG)

