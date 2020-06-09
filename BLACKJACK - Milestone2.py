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
        # for debugging purposes, print the deck
        print("######## DECK START ########")
        for suit in suits:
            for rank in ranks:
                print(Card(suit, rank))
        return "########## DECK END ###########"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        # remove a card from the deck
        return(self.deck.pop())

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # if higher than 21, if there are aces, we can readjust aces to be equal to 1
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips():

    # default chip num is 100
    def __init__(self):
        print("you start with 100 chips")
        self.total = 100
        self.bet = 0

    # might have to change the rules for wining the bet
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# declare the amount of chips to be bet
def take_bet(chips):
    while True:
        try:
            chips.bet = int(
                input("how many chips would you like to bet? "))
        except:
            print("this will not work, enter an intger")
        else:
            if chips.bet > chips.total:
                print("you dont have enough chips to bet. Bet at most {}, the amount you have.".format(
                    chips.total))
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        answer = input("\nhit or stand? enter h or s \n")

        if answer[0].lower() == "h":
            hit(deck, hand)
        elif answer[0].lower() == "s":
            print("Player Stands, Dealer turn")
            playing = False
        else:
            print("not a good input, enter smthg valid. ")
            continue

        break


def show_some(player_hand, dealer_hand):
    print("\nDEALER CARDS.")
    print("<hidden>")
    print(dealer_hand.cards[1])
    print("\nPLAYER CARDS")
    for card in player_hand.cards:
        print(card)


def show_all(player_hand, dealer_hand):
    print("\nDEALER CARDS:")
    for card in dealer_hand.cards:
        print(card)
    print("\nPLAYER CARDS")
    for card in player_hand.cards:
        print(card)


def player_busts(player_hand, dealer_hand, chips):
    print("PLAYER BUST")
    chips.lose_bet()


def player_wins(player_hand, dealer_hand, chips):
    print("PLAYER WINS")
    chips.win_bet()


def dealer_busts(player_hand, dealer_hand, chips):
    print("DEALER BUSTS")
    chips.win_bet()


def dealer_wins(player_hand, dealer_hand, chips):
    print("DEALER WINS")
    chips.lose_bet()


def push(player_hand, dealer_hand):
    print("PLAYER AND DEALER TIE, PUSH")


# game start


print("LETS PLAY BLACKJACK")
playing = True

# create and shuffle the deck
game_deck = Deck()
game_deck.shuffle()

# create a hand for the dealer and the player, and add two cards each
player_hand = Hand()
player_hand.add_card(game_deck.deal())
player_hand.add_card(game_deck.deal())

dealer_hand = Hand()
dealer_hand.add_card(game_deck.deal())
dealer_hand.add_card(game_deck.deal())

# player chips, default is 100
player_chips = Chips()

# place bets
take_bet(player_chips)

# show soem cards
show_some(player_hand, dealer_hand)

# player turn
while True:

    while playing:
        hit_or_stand(game_deck, player_hand)
        show_some(player_hand, dealer_hand)

        # bust
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(game_deck, dealer_hand)
        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print("\nYou now have {} chips".format(player_chips.total))

    play_again = input("would you like to play another hand? y/n ")

    if(play_again[0].lower() == "y"):
        playing = True
        continue
    else:
        print("thanks for playing. Youve won with {} chips".format(
            player_chips.total))
