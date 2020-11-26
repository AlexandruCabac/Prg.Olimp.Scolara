import array
n=int(input())
for k in range(1,n//2+1):
    x=k
    s=x
    while s<n:
        x+=1
        s+=x
    if s==n:
        print(f"{n}=",end='')
        for i in range(k,x):
            print(f"{i}+",end='')
        print(x)