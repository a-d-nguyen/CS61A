def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    n, common =1, 0
    def divisor (n, common):
        while n <= a and n <= b:
            if a % n == 0 and b % n == 0:
                common = n
                return divisor(n+1, common)
            else:
                return divisor(n+1, common)
        return common

    return divisor(n, common)


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print (n)
    if n == 1:
        return 1
    elif n%2 == 0:
        return 1 + hailstone(n//2)
    else:
        return 1 + hailstone (3 * n + 1)
