import re
from tabnanny import check
passw='mousavi.nsm@gmail@.com'
check=re.fullmatch('[a-zA-Z]+[-_.][a-zA-Z]+@[a-zA-Z]+[-_.]?[a-zA-Z]+\.[a-zA-Z]{2,5}', passw)

print(check)
if check==None:
    raise ValueError('invalid email !')
# def r(*arg):
#     print(arg) 
# r('dsfsdf',23,'dsfds')