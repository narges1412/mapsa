str=input('enter your string:')
str=' '.join(str)
str_list=str.split()
print(str_list)
def Wellـdefined(str):

    for i in range(0,len(str_list)):
        # if str[i]!=str[i+1]:
            if str_list[i]=='?':
                str_list[i]='0'
                if str_list[i-1]=='0' and str_list[i+1]=='0':
                    str_list[i]='1'
                    print('Wellـdefined!')
                if str_list[i-1]=='1' and str_list[i+1]=='0':
                    print('not Wellـdefined! ')
                if str_list[i-1]=='0' and str_list[i+1]=='1':
                    print ('not Wellـdefined! ')
                if str_list[i-1]=='0' and str_list[i+1]=='?' and str_list[i+2]=='1': 
                    str_list[i]='1'
                    str_list[i+1]='0'
                    print('Wellـdefined!')
                if str_list[i-1]=='1' and str_list[i+1]=='?' and str_list[i+2]=='0':
                    str_list[i]='0'
                    str_list[i+1]='1'
                    print('Wellـdefined!')


Wellـdefined(str_list)