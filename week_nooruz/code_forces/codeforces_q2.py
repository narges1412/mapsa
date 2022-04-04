n=input('enter a number:')
n=' '.join(n)
list1 = n.split()
map_object = map(int, list1)
listofint = list(map_object)
listofint.append(27)
# print(listofint)
def short_num(num):
    xlen=len(num)
    Comparison_list=[]
    for i in range(0,len(listofint)-1):
        if i!=27:
            Comparison_list.append(listofint[i]+listofint[i+1])
              
    Comparison_list. pop()
    # print (Comparison_list) 
    max_val=max(Comparison_list)
    index_max=Comparison_list.index(max_val)
    # print(index_max)
    listofint.pop()
    a=index_max+1
    listofint[a]=max_val
    listofint.pop(index_max)
    # print(listofint)
    str_show=''.join(map(str,listofint))
    print(str_show)
    



short_num(listofint)