n=int(input())
x=y=0
for k in range(0,n):
    d,p=map(int,input().split())
    if d==1:
        y+=p
    elif d==2:
        y+=p
        x+=p
    elif d==3:
        x+=p
    elif d==4:
        y-=p
        x+=p
    elif d==5:
        y-=p
    elif d==6:
        y-=p
        x-=p
    elif d==7:
        x-=p
    else:
        y-=p
        x-=p
print(x,y)