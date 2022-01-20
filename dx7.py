import random
x=[random.randint(1,200) for _ in range(50)]
kol=0
for i in range(1,len(x)-1):
    if x[i-1]<x[i]>x[i+1]:
        kol +=1

print(kol)
print(x)