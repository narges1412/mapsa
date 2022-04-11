

# Enter your code here. Read input from STDIN. Print output to STDOUT
# k,arr = int(input()),list(map(int, input().split()))

# myset = set(arr)

# print(((sum(myset)*k)-(sum(arr)))//(k-1))
counts = dict()
n = input()
number = input().split()
for i in number:
    if i not in counts:
        counts[i] = 1
       
    else:
        counts[i] += 1
        
for i in counts:
    if counts[i] == 1:
        print (i)
