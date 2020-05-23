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


a_coin = Coin()

while True:
    try:
        times = int(
            input("how many times would you like to flip a coin: (enter an integer) "))
        break
    except:
        print("integer please")

a_coin.flip(times)

print("well i mean thats all there is oto it man")
