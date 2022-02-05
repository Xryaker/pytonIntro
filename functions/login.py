c_m = {
    'lod': '123',
    'ele': '345',
    'ali': '456',
    'abq': '567',
    'amr': '678'
}


def chek_pass(usr, pas):
    if c_m.get(usr, False):
        if c_m.get(usr) == pas:
            return True
    else:
        return False


def decorator(func):
    def wrapper(usr, pas):
        if chek_pass(usr, pas):
            return True
        else:
            return False

    return wrapper


@decorator
def login():
    return
