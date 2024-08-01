import random


def sifre(a):
    characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    b  = ""
    for i in range(a):
        b += random.choice(characters)
    return b
