from collections import namedtuple
import random


def card_1():

    Card = namedtuple('Card', ['value', 'suit'])
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    cards = [Card(value, suit) for value in range(1,14) for suit in suits]

    x = (random.choice(cards)[0])
    y = (random.choice(suits))
    if x == 11:
        x = 'Queen'
    elif x == 12:
        x = 'King'
    elif x == 13:
        x = 'Jak'
    elif x == 14:
        x = 'Ace'
    else:
        x = x
    print(x, " of ", y)


def card_2():

    values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    deck = [[v + ' of ' + s,v] for s in suites for v in values]
    print(random.choice(deck))


card_1()
card_2()