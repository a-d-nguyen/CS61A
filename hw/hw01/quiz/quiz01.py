def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """

    x = 1
    while  (x % a != 0 or x % b != 0):
        x = x + 1

    return x

def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"

    nlist = [int(x) for x in str(n)]
    total , x , y = 0 , 0 , 0
    uni = []

    while y <=len(nlist):
        if y >= len(nlist):
            x, y = x + 1 , 0
        elif x == nlist[y]:
            uni = uni + [x]
            total = total + 1
            x , y = x + 1 , 0
        elif x > 9:
            return total
        else:
            y = y + 1

