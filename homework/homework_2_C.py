a=input()
h=[]
d=0
for x in a:
    h.extend(x)
for i in range(0,len(h)):
    if h[i].isupper()==False:
        d+=1
        i+=1
    else:
        b=a[d-len(h):]
r=0        
if b[-1]==".":
    k=b
else:
    for i in range(0,len(b)):
        if b[i]!=".":
            r+=1 
            i+=1
        else:
            k=b[:r+1-len(b)]  
for i in range(2,len(k)):
    l=k[::i]
    if l[-1]==".":
        print(l)
    else:
        l=0
        i+=1  
