#!/usr/bin/python3
"""
Define isWinner function, a solution to the Prime Game problem
and Ben must win
"""


def primes(n):
    """Return list of prime numbers between 1 and n inclusive.

    Args:
        n (int): The upper boundary of the range.
        The lower boundary is always 1.

    Returns:
        list: A list of prime numbers between 1 and n inclusive.
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): Number of rounds of the game.
        nums (list): List of integers representing the
        upper limit of the range for each round.

    Returns:
        str: Name of the winner ('Maria' or 'Ben') or
        None if the winner cannot be determined.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
