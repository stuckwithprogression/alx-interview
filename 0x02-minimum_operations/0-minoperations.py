#!/usr/bin/python3
'''minimum operarions
'''


def minOperations(n):
    '''calculates the fewest number of operations needed to result in exactly n
    H characters in a file
    '''

    i = 0
    j = 2

    while n > 1:
        while n % j == 0:
            i += j
            n = n / j

        j += 1

    return i
