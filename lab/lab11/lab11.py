def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    while n >= 0:
        yield n
        n -= 1

def trap(s, k):
    """Return a generator that yields the first K values in iterable S,
    but raises a ValueError exception if any more values are requested.

    >>> t = trap([3, 2, 1], 2)
    >>> next(t)
    3
    >>> next(t)
    2
    >>> next(t)
    ValueError
    >>> list(trap(range(5), 5))
    ValueError
    """
    assert len(s) >= k
    i = 0
    while k:
        yield s[i]
        i += 1
        k -= 1
    raise ValueError


def repeated(t, k):
    """Return the first value in iterable T that appears K times in a row.

    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(trap(s, 7), 2)
    4
    >>> repeated(trap(s, 10), 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1
    if type(t) is list:
        i, count = 0 , 1
        while i < len(t):
            if t[i] == t[i+1]:
                count += 1
                if count ==k:
                    return t[i]
            else:
                count, i = 1, i +1
        return
    prev, count = int(next(t)), 1
    while t:
        curr = int(next(t))
        if prev == curr:
            count += 1
            if count == k:
                return prev
        else:
            count, prev = 1, curr

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    while n > 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = n*3 +1
    yield n
