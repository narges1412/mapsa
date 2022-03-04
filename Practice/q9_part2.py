def parallelogram(a,b):
    for i in range(1, b+1):
         print(' ' * (b+1-i) + '* ' * (a) + ' ' * i)
parallelogram(5,4)