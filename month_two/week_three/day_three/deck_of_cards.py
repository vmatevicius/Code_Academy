# Create a deck of cards class.
# Internally, the deck of cards should use another class, a card class.
# Your requirements are:
#     The Deck class should have a deal method to deal a single card from the deckAfter a card is dealt, it is removed from the deck.
#     There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
#     The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

from typing import Union


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    VALUES = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    def __init__(self) -> None:
        self.deck = []
        self.build_deck()

    def build_deck(self) -> None:
        for suit in self.SUITS:
            for value in self.VALUES:
                self.deck.append(Card(suit, value))

    def deal(self) -> None:
        pass

    def shuffle(self) -> None:
        pass


class Card:
    def __init__(self, suit: str, value: Union[str, int]):
        self.suit = suit
        self.value = value
