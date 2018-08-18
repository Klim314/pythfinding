def identity(*args, **kwargs):
    return 0


def manhattan(c1, c2):
    """
    @args
        c1 (tuple): Coordinates of form (i, j)
        c2 (tuple): Coordinates of form (i, j)
    """
    i1, j1, = c1
    i2, j2 = c2
    return abs(i2 - i1) + abs(j2 - j1)