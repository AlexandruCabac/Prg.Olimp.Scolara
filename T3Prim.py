import math
n=int(input())
q=k=z=x=a=b=0
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        q=1
        break
    if(i==int(math.sqrt(n))-1 and q==0):
        a=n
        z=1
while q==1:
    k+=1
    a=n-k
    for l in range(2,int(math.sqrt(a))+1):
        if a%l==0:
            z=0
        else:
            z=1
            q=0
        if z==0:
            q=1
            break
    if q==0:
        break
    b=n+k
    for l in range(2,int(math.sqrt(b))+1):
        if b%l==0:
            x=0
        else:
            x=1
            q=0
        if x==0:
            q=1
            break
if((z==1 and z==x) or (z==1 and x==0)):
    print(a)
else:
    print(b)