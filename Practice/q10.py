msg='Babak Khorramdin'
print('harfe aval :',msg[0])
print('harfe K:',msg[6])
for i in range(0,len(msg)-3,2):
    print(msg[i], end=' ')
print()
if 'Babak'and 'Khorramdin' in msg:
    print('kalame babak va Khorramdin chap shod!')

for j in msg:
    if j=='m':
        print('True')
        break

