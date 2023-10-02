# import random
from random import randint

def dice():
    # result = random.randint(1, 6)
    result = randint(1, 6)
    return result

def dice2(faces=6):
    result = randint(1, faces)
    return result

def dice3(dice_number: int = 1, faces : int = 6) -> int:
    total = 0

    for i in range(dice_number):
        total += randint(1, faces)

    return total

d = dice3(3, 6)
print(d)