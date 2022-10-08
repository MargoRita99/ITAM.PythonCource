s=int(input())
k=0 #очники
h=0 #заочники
g=0 #?
while s!=0:
    a,b,c,d=input().split(" ")
    if d=="True" or d=="False":
        if d=="True":
            k+=1
        else:
            h+=1
    else:
        g+=1             
    s-=1
print(k,h,g)
