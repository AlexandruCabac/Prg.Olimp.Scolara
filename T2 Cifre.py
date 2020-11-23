import array
n=int(input())
a=array.array('i',)
x=m=p=0
for i in range(0,10):
    a.append(x)
while n>0:
    x=int(n%10)
    n=n//10
    a[x]+=1
m=a[0]
for x in range(1,10):
    if m<a[x]:
        p=x
        m=a[x]
print(p)