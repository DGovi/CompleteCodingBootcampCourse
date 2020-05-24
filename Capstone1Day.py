# coin flip simulation
# ask user how many times he wants ot flip a coin
# record the amount of times its heads and tails

import random

class Coin():

    def __init__(self):
        self.num_faces = 0
        self.num_tails = 0

    def flip(self, times_to_flip_coin):
        for n in range(times_to_flip_coin):
            heads_or_tails = random.randint(1, 2)
            if heads_or_tails == 1:
                self.num_faces += 1
            else:
                self.num_tails += 1
            print("heads: {}     tails: {}".format(
                self.num_faces, self.num_tails))

    def ask_play_again(self):
        answer = input(
            "would you like top flip the coin again? (y or yes if so) ")

        if answer[0].lower() == 'y':
            self.num_faces = 0
            self.num_tails = 0
            return True
        else:
            return False


a_coin = Coin()
flip_again = True

while flip_again:
    while True:
        try:
            times = int(
                input("how many times would you like to flip a coin: (enter an integer) "))
            break
        except:
            print("integer please")

    a_coin.flip(times)
    flip_again = a_coin.ask_play_again()

print("Thanks for using coin fliip simulator")
