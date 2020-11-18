n=int(input('n='))
s=b=c=x=0
for i in range(1,n+1):
    if(n%i==0):
        s+=i
for k in range(2,s):
    if(s%k==0):
        b=1
if(b==0):
    while n>0:
        c=c+n%10
        n=n//10
else:
    while n>0:
        x=n%10
        n=n//10
        if(x%2==1):
            c=x+c
print(c)