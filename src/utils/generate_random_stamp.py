import random

from src.config.config import STAMP_SIZE


def generator_random_stamp(n=STAMP_SIZE):
    randomlist = []
    for _ in range(0, 5):
        n = random.randint(0, 10)
        randomlist.append(n)
    randomstring = "".join([str(n) for n in randomlist])
    return randomstring
