from typyboi.items import Item, Weapon
from typyboi.enemies import Enemy

def dagger():
    return Weapon('Dagger', 'A sharp but short dagger', 5, 5)

def spider():
    return Enemy('Spider', 10, 2)