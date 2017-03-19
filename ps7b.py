#  probability of rolling a Yahtzee! on the first roll ?
# Yahtzee is having five-of-kind when rolling 5 dices
# example : <1,1,1,1,1> or <3,3,3,3,3> etc. ..

import random


def roll():
    return random.choice([1,2,3,4,5,6])


def YahtzeeSim(trials=1000000):
    yatzhee = 0.0
    for i in range(trials):
        d1 = roll()
        d2 = roll()
        d3 = roll()
        d4 = roll()
        d5 = roll()
        if d1 == d2 == d3 == d4 == d5:
            yatzhee += 1
    return yatzhee/trials

## print YahtzeeSim()

