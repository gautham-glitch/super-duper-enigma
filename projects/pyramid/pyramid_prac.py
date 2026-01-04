#floyd
rows = 3
terms = ((rows+1)*rows)//2
list = []
i = 1
while i <= terms:
    list.append(i)
    i+=1
i = 0
for x in range(0,rows+1):
    for j in range(x):
        print(list[i], end=" ")
        i+=1
    print()
#pascal
for n in range(1,rows+1):
    c = 1
    for i in range(1,n+1):
        print(c,end=" ")
        c = c*(n-i)//i
    print()
