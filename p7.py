##--------------------------CLASS THAT TAKES NAME AND MARKS OF 3 SUBJECTS AS ATTRIBUTE PRINT THE AVERAGE IN METHOD----------------##
class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def cal_average(self):
        return (self.marks1+self.marks2+self.marks3)/3
    
s1=Student("Scheeza",43,89,56)
print(s1.cal_average())    

##-----------------------Create a bank account with two attributes balance and account no .Create methods for debit credit and balance--------------##
class Bank:
    balance=0
    account_no=0
    def __init__(self,balance,account_no,am_debit,am_credit):
        self.balance=balance
        self.account_no=account_no
        self.am_debit=am_debit
        self.am_credit=am_credit

        # self.amount=amount
    def debit(self):
        return (self.balance+self.am_debit)
    def credit(self):
        return self.balance+self.am_credit
    def bal(self):
        if self.credit():
            return self.balance+self.am_credit
        else:
            return self.balance-self.am_debit


    
b1=Bank(1200,1234,100,200)
print(b1.balance,b1.account_no)    
print("The amount after debit is : ",b1.debit())
print("The balnce in the bank  is : ",b1.bal())

print("The amount after credit is : ",b1.credit())
print("The balnce in the bank  is : ",b1.bal())



    
