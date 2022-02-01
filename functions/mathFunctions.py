def multiplication(a):
    """

    :tbpe a: string
    """
    multi = 1
    for i in a:
        if int(i) != 0:
            multi *= int(i)
    return multi


def arithmetic(u):
    """

    :param u: tuple 3 itemms 1st digit, 2nd digit, 3mathSymbol
    :return: arifmetic result
    """
    a, b, c = u
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b
