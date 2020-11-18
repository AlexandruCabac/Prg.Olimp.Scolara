a=int(input())
b=int(input())
c1=c2=x=0
while a>0:
    c1=a%10
    a=a//10
    c2=b%10
    b=b//10
    if(c1!=c2):
        x+=1
print("Trebuie de schimbat",x,"cifre")