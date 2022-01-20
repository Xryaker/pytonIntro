import random
x=int(input("Введите рост Пети: "))
list_students=[random.randint(50,200) for _ in range(30)]
list_students.append(x)
list_students.sort(reverse=True)
print("Номер в строю: ")
print(list_students.index(x)+(list_students.count(x)-1)+1)
print(list_students)
