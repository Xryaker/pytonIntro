imput_txt = input("Введите что-нибудь: ")
txt = f"Внимание \"{imput_txt}\" - Это то, что вы только что ввели в строку"
print(txt)
txt = txt.replace(imput_txt, "замена в строке")
print(txt)
print(len(txt))
if txt.find("строка") == -1:
    print("НЕТ")
else:
    print("ДА")
