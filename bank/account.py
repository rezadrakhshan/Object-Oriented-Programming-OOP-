import random
from bank import BankAccount
list = ["0","1","2","3","4","5","6","7","8","9"]

class person:
    product_list = []
    def __init__(self,name,id,mablagh) :
        self.bank = BankAccount()
        self.name = name
        self.id = id
        self.mablagh = mablagh
        temp  = "4444"
        for i in range(12):
            temp += random.choice(list)
        self.credit_number = int(temp)

    def add(self,mablagh):
        self.bank.variz(self.name,self.id,self.credit_number,927949729247924794,mablagh)
        self.product_list.append(self.name)
        return self.product_list



