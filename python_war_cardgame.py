import random
from collections import namedtuple
"""
This is a card game war for python

"""

playerA = []
playerb = []


def splitdeck():
    Card = namedtuple('Card', ['value', 'suit'])
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    cards = [Card(value, suit) for value in range(1, 14) for suit in suits]

    x = (random.choice(cards)[0])
    y = (random.choice(suits))

    print(x)


def war():
    pass