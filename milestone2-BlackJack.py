import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)


class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                newCard = Card(suit, rank)
                self.deck.append(newCard)

    def __str__(self):
        print("######## DECK START ########")
        for suit in suits:
            for rank in ranks:
                print(Card(suit, rank))
        return "########## DECK END ###########"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return(self.deck.pop())

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        if self.value > 21:
            values.Ace = 1
        else:
            values.Ace = 11

class Chips():

    # default chip num is 100
    def __init__(self):
        self.total = 100
        self.bet = 0

    # might have to change the rules for wining the bet
    def win_bet(self):
        self.total = self.total + self.bet

    def lose_bet(self):
        self.total = self.total - self.total
