# Himanshu Sekhar Nayak
# REGD_NO: 2241014080

import random
from enum import Enum

class Suit(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

class Rank(Enum):
    ACE = "Ace"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank.value} of {self.suit.value}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        if card:
            self.hand.append(card)

    def get_hand_value(self):
        value = 0
        aces = 0
        
        card_values = {Rank.ACE: 11, Rank.TWO: 2, Rank.THREE: 3, Rank.FOUR: 4, Rank.FIVE: 5,
                       Rank.SIX: 6, Rank.SEVEN: 7, Rank.EIGHT: 8, Rank.NINE: 9, Rank.TEN: 10,
                       Rank.JACK: 10, Rank.QUEEN: 10, Rank.KING: 10}
        
        for card in self.hand:
            value += card_values[card.rank]
            if card.rank == Rank.ACE:
                aces += 1
        
        while value > 21 and aces:
            value -= 10
            aces -= 1
        
        return value

    def is_busted(self):
        return self.get_hand_value() > 21

class BlackjackGame:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.dealer = Player("Dealer")

    def deal_initial_cards(self):
        for _ in range(2):
            for player in self.players:
                player.add_card(self.deck.draw_card())
            self.dealer.add_card(self.deck.draw_card())

    def play(self):
        self.deal_initial_cards()
        for player in self.players:
            while player.get_hand_value() < 21:
                action = input(f"{player.name}, do you want to hit or stand? (h/s): ")
                if action.lower() == 'h':
                    player.add_card(self.deck.draw_card())
                    print(f"{player.name}'s hand: {player.hand}, Total: {player.get_hand_value()}")
                    if player.is_busted():
                        print(f"{player.name} busts!")
                        break
                else:
                    break
        
        while self.dealer.get_hand_value() < 17:
            self.dealer.add_card(self.deck.draw_card())
        print(f"Dealer's hand: {self.dealer.hand}, Total: {self.dealer.get_hand_value()}")
        
        for player in self.players:
            if not player.is_busted():
                if player.get_hand_value() > self.dealer.get_hand_value() or self.dealer.is_busted():
                    print(f"{player.name} wins!")
                elif player.get_hand_value() < self.dealer.get_hand_value():
                    print(f"{player.name} loses!")
                else:
                    print(f"{player.name} ties with the dealer!")

if __name__ == "__main__":
    player_names = input("Enter player names separated by commas: ").split(",")
    game = BlackjackGame(player_names)
    game.play()
