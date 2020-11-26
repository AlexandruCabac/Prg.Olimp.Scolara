import math
b=str(input())
a=len(b)
q=0
for i in range(-1,-a-1,-2):
    b=b[:a+i]+b[a+i+1:]
for k in range(2,int(math.sqrt(int(b)))+1):
    if int(b)%k==0:
        q+=1
if q==0:
    print("Yes")
else:
    print("No")