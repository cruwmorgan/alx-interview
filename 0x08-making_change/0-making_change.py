#!/usr/bin/python3
"""
    script that determine the fewest number of coins needed to meet a
    given amount total.
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """ take  a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
        Args:
            coins: a list of the values of the coins in your possession
            total: given amount
        Return:
            0 or fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    else:
        coin = sorted(coins)
        coin.reverse()
        counter: int = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
