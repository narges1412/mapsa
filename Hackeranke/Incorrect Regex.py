import re
from unittest import result
n=int(input())
for i in range(n):
    test=input()

    result1=re.compile(test)
    if result1:
        print('True')
    else:
        print('False')
#print(result1)
