# The initiation of Bridge game.
# It requires 4 players, one of them is called the declarer.
# Every player gets 13 cards.

import random


def pick_a_card(deck, picked_card):
    ''' (list, list) -> str
    Return a random card from deck, excluding those in picked_card,


    '''
    # create a clone of the deck
    temp_deck = list(deck)
    # remove the picked cards from the deck
    for item in picked_card:
        temp_deck.remove(item)
    # generate a random number between 0-lenght of temp_deck
    rand = random.randint(0, len(temp_deck) - 1)
    # pick a card
    card = temp_deck[rand]
    # return the picked card
    return card


# declare ranks and suits
rank = ["2", "3", "4", "5", "6", "7", "8", "9",
        "10", "Jack", "Queen", "King", "Ace"]

suit = ["Clubs", "Diamonds", "Hearts", "Spades"]

# creates a deck in the following order
'''
['2 of Clubs', '2 of Diamonds', '2 of Hearts', '2 of Spades', '3 of Clubs',
'3 of Diamonds', '3 of Hearts', '3 of Spades', '4 of Clubs', '4 of Diamonds',
'4 of Hearts', '4 of Spades', '5 of Clubs', '5 of Diamonds', '5 of Hearts',
'5 of Spades', '6 of Clubs', '6 of Diamonds', '6 of Hearts', '6 of Spades',
'7 of Clubs', '7 of Diamonds', '7 of Hearts', '7 of Spades', '8 of Clubs',
'8 of Diamonds', '8 of Hearts', '8 of Spades', '9 of Clubs', '9 of Diamonds',
'9 of Hearts', '9 of Spades', '10 of Clubs', '10 of Diamonds', '10 of Hearts',
'10 of Spades', 'Jack of Clubs', 'Jack of Diamonds', 'Jack of Hearts',
'Jack of Spades', 'Queen of Clubs', 'Queen of Diamonds', 'Queen of Hearts',
'Queen of Spades', 'King of Clubs', 'King of Diamonds', 'King of Hearts',
'King of Spades', 'Ace of Clubs', 'Ace of Diamonds', 'Ace of Hearts',
'Ace of Spades']
'''
deck = []
for rank_item in rank:
    for suit_item in suit:
        deck.append(rank_item + " of " + suit_item)

# shuffle the deck, do not use python's shuffle function
# swap each item with a random item in the list
for i in range(0, len(deck)):
    rand = random.randint(0, len(deck)-1)  # [0, 51]
    temp = deck[i]
    deck[i] = deck[rand]
    deck[rand] = temp

# Declarer is the one who tells which suit is the trump.
# For now, the person who gets ace of spades will be the declarer
# players keep deal out one card at a time, until one of them becomes
# a declarer.
# the first picked cards is for player_0, 2nd for player_1, 3rd for
# player_2, 4th for player_3


picked_card_list = []
picked_card = ""
ace_of_spades = 'Ace of Spades'
player_turn = -1
# player_turn = 0 represents player 1, so player_turn = 3 represents player 4
while (picked_card != ace_of_spades):
    player_turn = (player_turn + 1) % 4
    picked_card = pick_a_card(deck, picked_card_list)
    picked_card_list.append(picked_card)

print ("Declarer is player", player_turn + 1,
       "becasue she picked the ",  picked_card, "\n")

# deal out 13 cards to each player
picked_card = []
player_0 = []
player_1 = []
player_2 = []
player_3 = []

for index in range(0, len(deck) // 4):
    card = pick_a_card(deck, picked_card)
    player_0.append(card)
    picked_card.append(card)
    card = pick_a_card(deck, picked_card)
    player_1.append(card)
    picked_card.append(card)
    card = pick_a_card(deck, picked_card)
    player_2.append(card)
    picked_card.append(card)
    card = pick_a_card(deck, picked_card)
    player_3.append(card)
    picked_card.append(card)

print("The first player's cards =", player_0, "\n")
print("The second player's cards =", player_1, "\n")
print("The third player's cards =", player_2, "\n")
print("The fourth player's cards =", player_3)
