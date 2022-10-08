a = list(map(int, input().split(" ")))
k=1
a.sort()
for i in range(0, len(a)-1):
    if a[i]!=a[i+1]:
        k+=1
    else:
        i+=1
print(k)    
