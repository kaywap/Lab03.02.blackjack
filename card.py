# Simulates a playing card
# Julian Cochran
# 04.08.2025
# includes operator overloads

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.raw_value = val  # Store the original value (2-14)

        # Set the display name
        if val == 11:
            self.name = "Jack of " + suit
        elif val == 12:
            self.name = "Queen of " + suit
        elif val == 13:
            self.name = "King of " + suit
        elif val == 14:
            self.name = "Ace of " + suit
        else:
            self.name = str(val) + " of " + suit

        # Set the blackjack value
        if val >= 11 and val <= 13:  # Face cards
            self.value = 10
        elif val == 14:  # Ace
            self.value = 11  # Default to 11, can be adjusted to 1 when needed
        else:
            self.value = val

        # Track if this is an ace that can be counted as 1
        self.is_ace = (val == 14)
        self.ace_as_one = False  # Track if we're counting this ace as 1 instead of 11

    def use_ace_as_one(self):
        """Convert this ace from 11 points to 1 point"""
        if self.is_ace and not self.ace_as_one:
            self.value = 1
            self.ace_as_one = True
            return True
        return False

    def reset_ace(self):
        """Reset ace to default value of 11"""
        if self.is_ace:
            self.value = 11
            self.ace_as_one = False

    def get_image_filename(self):
        """Return the filename for this card's image"""
        if self.raw_value == 11:
            value_str = "jack"
        elif self.raw_value == 12:
            value_str = "queen"
        elif self.raw_value == 13:
            value_str = "king"
        elif self.raw_value == 14:
            value_str = "ace"
        else:
            value_str = str(self.raw_value)

        return f"{value_str}_of_{self.suit.lower()}.png"

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value