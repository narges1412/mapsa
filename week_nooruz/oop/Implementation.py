import re
from Acount import Acount
from Site import Site
x=Acount('jfj_p','aA123123','+989105364966','mousa.nsm@gmail.com')
#x.check_username()
# x.check_password()
# x.check_phone()
#x.check_email()

s=Site('www.google.com','jfjwe_r',3)
s.register(x)