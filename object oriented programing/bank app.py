

class bank:
    bank_name="sbk"

    def __init__ (self,accno,person_name,balance):
        self.accno=accno
        self.person_name=person_name
        self.balance=balance


    def deposit(self,amount):
        self.balance+=amount
        print(self.bank_name,"your account",self.accno,"has been credited with",amount,"you balance is",self.balance)


    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balane")
        else:


            self.balance-=amount
            print("your account",self.accno,"has been withdrwaed with",amount,"you balance is",self.balance)

    def balnceenq(self):
        print("current balance",self.balance)


obj=bank(1000,"ajay",2000)

obj.balnceenq()
obj.deposit(2000)
obj.withdraw((1000))
obj.balnceenq()
