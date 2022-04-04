n=int(input('enter a number for list:'))
list=[]
count=0
for i in range(0,n):
    list.append(int(input()))
for i in range(0,n):
    if list[i]!=list[0] and list[i]!=list[n-1]:
        if list[i]>list[i+1] and list[i]>list[i-1]:
            list[i]=list[i]+1
            count+=1
print(list)
print(count)



                                                           