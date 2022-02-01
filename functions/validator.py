def validateInputArg():
    x = input("Введите перво число: ")
    if not x.isdigit():
        print("Первый символне не число")
        quit(-1)
    y = input("Введите второе чиcло: ")
    if not y.isdigit():
        print("Второй символ не число")
        quit(-1)
    z = input("Введите знак(+, -): ")
    if not z == "+" or z == "-" or z == "/":
        print("Неизвестная операция")
        quit(-1)
    if z == "/" and y == 0:
        print("На 0 делить нельзя")
        quit(-1)
    return int(x), int(y), z
