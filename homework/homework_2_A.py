s=int(input())
k=0 #очный
h=0 #заочный
while s!=0:
    a,b,c,d=input().split(" ")
    if d=="True":
        k+=1
    else:
        h+=1
    s-=1    
print(k,h)
