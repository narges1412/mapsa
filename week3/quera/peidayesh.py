num1=int(input('ali enter your number:'))
if num1 >5:
    print('enter number between 1,4')
num2=int(input('meli enter your mumber:'))
if num2 >5:
    print('enter number between 1,4')
num3=int(input('salib enter your number:'))
if num3 >5:
    print('enter number between 1,4')
list=[1,2,3,4]


    
        
                


def find(num1,num2,num3):

    for i in range(1,5):
        if i==num1 or i==num2 or i==num3:
            list.remove(i)
    print('next number is',list)          
    return list
      


    
find(num1,num2,num3)