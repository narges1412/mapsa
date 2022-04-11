
n,M = map(int,input().split())
lines = []
for i in range(0,n):
    lines.append(list(map(int,input().split())))   
K=int(input())
lines = sorted(lines,key = lambda x: x[K])
for line in lines:
    print (' '.join(str(k) for k in line))