def multiplication (x):
    """

    :type x: string
    """
    multi = 1
    for i in x:
        if int(i) != 0:
            multi *= int(i)
    return multi


