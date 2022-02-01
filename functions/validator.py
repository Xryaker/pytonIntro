def validateInputArg():
    x = input("Введите перво число: ")
    y = input("Введите второе чиcло: ")
    z = input("Введите знак(+, -): ")
    if not x.isdigit():
        print("Первый символне не число")
        return False
    if not y.isdigit():
        print("Второй символ не число")
        return False
    if not z == "+" or z == "-" or z == "/":
        print("Третий знак не математический символ")
        return False
    return int(x), int(y), z
