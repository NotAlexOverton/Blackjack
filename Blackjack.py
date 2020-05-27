import random as r
import itertools

# cards and their values
Cards = {
    "Ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}
# define card suits
Suits = ["Hearts", "Clubs", "Spades", "Diamonds"]

# find keys for dictionary
keys = Cards.keys()

# generate deck of cards
deck = set(itertools.product(keys, Suits))

# draw a random card from the set
def DrawCard():
    card = deck.pop()
    return card

# initialise hand values
hand_value_player = 0
hand_value_dealer = 0

print("Welcome to blackjack!")

# dealer draws 1
(face, suit) = DrawCard()
print("Dealer draws: " + face + " of " + suit)
hand_value_dealer = hand_value_dealer + Cards[face]
print("Hand value: " + str(hand_value_dealer))

# player draws 2
(face, suit) = DrawCard()
(face2, suit2) = DrawCard()
print("You draw: " + face + " of " + suit + " and " + face2 + " of " + suit2)
hand_value_player = hand_value_player + Cards[face] + Cards[face2]

# initialise stick booleans
player_stick = False
dealer_stick = False

# while still playing, play more!
while player_stick == False:
    print("Hand value: " + str(hand_value_player))
    print("Draw another card? (Y/N)")

    if str(input("")) == ("Y" or "y"):
        (face, suit) = DrawCard()
        print("You draw: " + face + " of " + suit)
        hand_value_player = hand_value_player + Cards[face]

        if hand_value_player == 21:
            print("21!")
            player_stick = True

        if hand_value_player > 21:
            print(str(hand_value_player) + ", bust!")
            player_stick = True

    else:
        print("Sticking on " + str(hand_value_player))
        player_stick = True


print("Dealer's turn!")

# dealer plays while he is allowed
while hand_value_dealer < 18 or dealer_stick == False:

    if hand_value_dealer < 18:
        (face, suit) = DrawCard()
        print("Dealer draws: " + face + " of " + suit)
        hand_value_dealer = hand_value_dealer + Cards[face]

        if hand_value_dealer == 21:
            print("21!")
            dealer_stick = True

        if hand_value_dealer > 21:
            print(str(hand_value_dealer) + ", bust!")
            dealer_stick = True

        else:
            print("Dealer hand value: " + str(hand_value_dealer))

    else:
        print("Sticking on " + str(hand_value_dealer))
        dealer_stick = True

# pikey solution
win = False

if (hand_value_player > 21 and hand_value_dealer > 21) or (hand_value_player <= 21 and hand_value_dealer > 21) or ((hand_value_player < 21 and hand_value_dealer < 21) and (hand_value_player > hand_value_dealer)):
    win = True
if win == True:
    print("You win!")
else:
    print("You lose!")