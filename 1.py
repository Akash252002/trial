import swap
s=input("enter string")
n=len(s)
i=0
j=n-1

while i<j:
    t=s[i]
    s[i]=s[j]
    s[j]=t
    i+=1
    j-=1

