import array
n=int(input())
p=m=0
a=array.array('B',)
for i in range(0,n):
    x=int(input())
    a.append(x)
for k in range(0,n-1):
    if(a[k+1]-a[k])>m:
        m=a[k+1]-a[k]
    if(a[k+1]-a[k])>1:
        p+=1
print(f"Nr minim de pastile este {p}, iar diferența maximă este {m}")