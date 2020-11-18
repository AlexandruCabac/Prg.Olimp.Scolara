k=int(input("k="))
c=s=a=0
while s<=k:
    a=int(input())
    c+=1
    if(a%2==0):
        s+=a
print("S-au introdus",c,"numere, iar suma nr. pare este",s)
