import random
x=[random.randint(1,200) for _ in range(10)]
y=[random.randint(1,200) for _ in range(10)]
print(len(set(x)&set(y)))
print(x)
print(y)
