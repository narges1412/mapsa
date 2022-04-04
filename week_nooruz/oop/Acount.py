from logging import exception
import re
from tabnanny import check

class Acount(object):
    save_username=[]
    save_email=[]
    def __init__(self,username,password,phone,email) -> None:
        self.username=username
        self.password=password
        self.phone=phone
        self.email=email

    def check_username(self):
        name=self.username
        check=re.fullmatch('[a-zA-z]+_[a-zA-z]+',name)
        if check==None:
            raise Exception("invalid username !")
        else:
            Acount.save_username.append(name) 
            

    def check_password(self):
        check_password=self.password
        check=re.fullmatch("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,20}$",check_password)
        if check==None:
            raise ValueError('invalid password !')
    
    def check_phone(self):
        # save_phone=[]
        check_phone=self.phone
        check=re.fullmatch('^([+989]{4}|[09]{2})\d{9}$',check_phone)
        if check==None:
            raise ValueError('invalid phone number !')
        else:
            if check_phone[0:4]=='+989':
                save_phone=[]
                check_phone=' '.join(check_phone)
                save_phone=check_phone.split(' ')
                save_phone[2]='0'
                save_phone.pop(0)
                save_phone.pop(0)
                save_phone=''.join(save_phone)
                
    
    def check_email(self):
        check_email=self.email
        check=re.fullmatch('[a-zA-Z]+[-_.][a-zA-Z]+@[a-zA-Z]+[-_.]?[a-zA-Z]+\.[a-zA-Z]{2,5}', check_email)
        if check==None:
            raise ValueError('invalid email !')
        else:
            Acount.save_email.append(check_email) 
        
        


