a = list(map(int, input().split(" ")))
h=a[-1:]+ a[0:len(a)-1]
for x in h:
    print(x, end=' ')
