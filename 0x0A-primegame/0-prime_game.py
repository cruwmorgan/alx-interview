#!/usr/bin/python3
"""
    script to find the winner pf a Prime game
"""


def primeNumbers(n):
    """ function to gcheck for prime number
    Args:
        n: upper boundary of range. lower boundary is always 1
    Return:
        True or False
    """
    primeNos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNos


def isWinner(x, nums):
    """ function to determine the winner
    Args:
        x: rounds of the game
        nums: upper boundary of range. lower boundary is always 1
    Returns:
        Ben or Maria as winner
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNos = primeNumbers(nums[i])
        if len(primeNos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
