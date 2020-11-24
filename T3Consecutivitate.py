s=str(input())
a=b=0
for i in range(0,len(s)):
    if(ord(s[i])>=48 and ord(s[i])<=57):
        a+=1
        b=b+ord(s[i])-48
print(a,b,sep='\n')