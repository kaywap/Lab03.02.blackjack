# hand.py
# simulates a player's hand of cards
# Julian Cochran
# 04.08.2025

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Add a card to the hand"""
        self.cards.append(card)

    def calculate_value(self):
        """Calculate the value of the hand, handling aces appropriately"""
        # First, reset all aces to their default value of 11
        for card in self.cards:
            if card.is_ace:
                card.reset_ace()

        # Calculate total value
        value = sum(card.value for card in self.cards)

        # If we're over 21, try to use aces as 1 instead of 11
        aces = [card for card in self.cards if card.is_ace and not card.ace_as_one]
        while value > 21 and aces:
            # Use one ace as 1 instead of 11 (reduces total by 10)
            ace = aces.pop()
            ace.use_ace_as_one()
            value -= 10

        return value

    def is_blackjack(self):
        """Check if this hand is a blackjack (21 with 2 cards)"""
        return len(self.cards) == 2 and self.calculate_value() == 21

    def is_busted(self):
        """Check if this hand is busted (over 21)"""
        return self.calculate_value() > 21

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)