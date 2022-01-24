import string, random

slowar1={random.choice(string.ascii_letters):random.randint(1,200) for _ in range(random.randint(10,30))}
slowar2={random.choice(string.ascii_letters):random.randint(1,200) for _ in range(random.randint(10,30))}
slowar3=slowar2
print(slowar1)
print(slowar2)
for i in slowar1:
    if slowar2.get(i)!=None:
        if slowar2.get(i)<slowar1.get(i):
            slowar3.update({i:slowar1.get(i)})
    else:
        slowar3.update({i:slowar1.get(i)})

print(slowar3)