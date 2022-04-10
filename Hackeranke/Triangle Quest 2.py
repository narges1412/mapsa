from itertools import count


n=int(input())
j=1
s = ""
count=0
for i in range(1,n+1):
    while j<=i:
        s+=str(i)
        j+=1
    revers=''.join(reversed(s))
    print(s,revers[1:])
# j=n
# while j>=1:
#     s+=str(j)  
#     j-=1 
   
  
