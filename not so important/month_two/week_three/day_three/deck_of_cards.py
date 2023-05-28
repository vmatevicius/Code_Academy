# Create a deck of cards class.
# Internally, the deck of cards should use another class, a card class.
# Your requirements are:
#     The Deck class should have a deal method to deal a single card from the deckAfter a card is dealt, it is removed from the deck.
#     There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
#     The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

from typing import Union, List
from random import randint


class Card:
    def __init__(self, suit: str, value: Union[str, int]):
        self.suit = suit
        self.value = value


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    VALUES = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    def __init__(self):
        self.deck = []
        self.build_deck()
        self.shuffled_deck = self.shuffle()

    def build_deck(self) -> None:
        for suit in self.SUITS:
            for value in self.VALUES:
                self.deck.append(Card(suit, value))

    def show_deck(self) -> None:
        for card in self.deck:
            print(f"{card.value} of {card.suit}")

    def deal(self) -> None:
        highest_index = len(self.shuffled_deck)
        random_index = randint(0, (highest_index - 1))

        print(
            f"Card dealt is {self.shuffled_deck[random_index].value} of {self.shuffled_deck[random_index].suit}"
        )
        self.shuffled_deck.remove(self.shuffled_deck[random_index])

    def shuffle(self) -> List[Card]:
        shuffled_deck = []
        random_index = randint(0, 51)
        used_indexes = []
        while len(used_indexes) != 52:
            if random_index not in used_indexes:
                shuffled_deck.append(self.deck[random_index])
                used_indexes.append(random_index)
            random_index = randint(0, 51)
        return shuffled_deck

    def show_shuffled_deck(self) -> None:
        for card in self.shuffled_deck:
            print(f"{card.value} of {card.suit}")


card = DeckOfCards()
card.shuffle()
card.deal()
