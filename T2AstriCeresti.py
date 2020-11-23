import array
a=[]
x=y=z=b=n=q=i=0
while b==0:
    x=str(input())
    if len(x)!=0:
        a.append(x)
        n+=1
        q=n
    else:
        b=1
while(b==1 and i<q):
    i+=1
    x=a[i-1]
    y=a[i]
    if ord(x[0])<ord(y[0]):
        z=a[i]
        a[i]=a[i-1]
        a[i-1]=z
        b=0
    elif ord(x[0])==ord(y[0]):
        if len(x)>len(y):
            z=a[i]
            a[i]=a[i-1]
            a[i-1]=z
            b=0
        elif len(x)==len(y):
            for k in range(1,len(x)):
                if ord(x[k])<ord(y[k]):
                    z=a[i]
                    a[i]=a[i-1]
                    a[i-1]=z                  
                    b=0
    if(i==q-1 and b==0):
        q-=1
        i=0
        b=1
x=a[0]
for j in range(1,n):
    x+=a[j]
print(x)