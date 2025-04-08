# deck.py
# simulates a deck of cards
# Julian Cochran
# 04.08.2025

import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """Create a new 52-card deck"""
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # 11=J, 12=Q, 13=K, 14=A

        self.cards = []
        for suit in suits:
            for val in values:
                self.cards.append(Card(suit, val))

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)

    def deal(self):
        """Deal one card from the deck"""
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None

    def __str__(self):
        return f"Deck with {len(self.cards)} cards remaining"