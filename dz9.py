sumwords ={}
for word in input().split():
    sumwords[word]=sumwords.get(word,0)+1
for i in sumwords:
    print(i, " = ", sumwords[i])
