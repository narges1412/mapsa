# class Clm():
#     pass
# a=Clm()
# print(a.__repr__)
class TrasnsactionBook:

   def __init__(self, user_id, shares=[]):

       self.user_id = user_id

       self.shares = shares

   def add_trade(self, name , quantity, buySell):

       self.shares.append([name,quantity,buySell])

   def __getitem__(self, i):

       return self.shares[i]

obj=TrasnsactionBook('USER1')
obj.add_trade('bitcoin',20,'B')
obj.add_trade('Tether',30,'S')
obj.add_trade('Doj',4,'B')
print(obj[1])


