x=int(input("Введите высоту пирамиды: "))
print("вариант А:")
w=x+(x-1)
for  i in range(x+1):
    print("{0:^{1}}".format("*"*(i+(i-1)),w))

print("вариант B:")
for  t in range(x):
    if t==0:
        print("{0:^{1}.{2}}".format("*",w,w))
    else:
        if t==x-1:
               print("{0:^{1}}".format("*"*(i+(i-1)),w))
        else:
             print("{0:^{1}.{2}}".format("*"+" "*(t+(t-1))+"*",w,w))

print("вариант C:")
for  i in range(x+1):
    print("{0:^{1}}".format("*"*(i+(i-1)),w))
o=(x-1)*2-3
for i in range(x-1):
                  if i==x-2:
                         print("{0:^{1}.{2}}".format("*",w,w))
                  else:
                       print("{0:^{1}.{2}}".format("*"+" "*(o)+"*",w,w))
                       o=o-2

print("вариант D:")
for  i in range(x+1):
    print("{0:^{1}}".format("*"*(i+(i-1)),w))
o=(x-1)*2-3
for i in range(x-1):

                  if i==x-2:
                         print("{0:^{1}.{2}}".format("*",w,w))
                  else:
                       str="{0:^{1}}".format("*",o)
                       str="{0:^{1}.{2}}".format("*"+str+"*",w,w)
                       print(str)
                       o=o-2
