from pexpect import ExceptionPexpect
from Acount import Acount
class Site(Acount):
    register_users=['jfjwe_r']
    def __init__(self,url,register_users,active_users) -> None:
        self.url=url
        self.register_users=register_users
        self.active_users=active_users
    
    def register(self,x):
        x.check_email()
        x.check_username()
        
        if Site.register_users==x.save_username:
            raise ValueError('user alredy registered !')
        else:
            Site.register_users.append(x.save_username) #self.register_users
            print('register successeful !')         
        
        if Site.register_users==x.save_email:
            raise ValueError('user alredy registered !')
        else:
            Site.register_users.append(x.save_email) #self.register_users
            print('register successeful !')  
            
        print(Site.register_users)

    def login(*arg):#فرض کنیم ترتیب ورودی ها به این صورت باشند:(email,username, pass)
        if arg[1] in Acount.save_email:
            pass
         

