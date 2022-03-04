num1=int(input('enter  number:'))
num2=int(input('enter  number:'))
num3=int(input('enter  number:'))
def minmax(num1,num2,num3):
    num_list=[num1,num2,num3]
    sort_list=sorted(num_list)
    print(f"max is:{sort_list[2]}")
    print(f"min is:{sort_list[0]}")
minmax(num1,num2,num3)