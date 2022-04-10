n, m = map(int,input().split())
ar = list(map(int,input().split()))

set_a=set(map(int,input().split()))
set_b=set(map(int,input().split()))
happiness=0
for i in ar:
    if i in set_a:
        happiness+=1
    if i in set_b:
        happiness-=1
print(happiness)
