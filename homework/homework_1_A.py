a = list(map(int, input().split(" ")))
h=a[1:len(a)]
for i in range(1,len(h)):
    if i%2!=0 and i!=0:
        i+1
    else:
        print(h[i], end=' ') 
