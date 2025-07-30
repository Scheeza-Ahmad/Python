##------------------------------------------DELETE KEYWORD----------------------------------##
#It is used to delete a keyword 

class Name:
    name="Scheeza"
n=Name()
print(n.name)
del n
# print(n.name)

##--------------------------------------PRIVATE AND PUBLIC----------------------------------##
#-->Private are used only inside the class and not outsie the class
#-->We use double underscore behind the name of the attribute or method to make it private

class Bank:
    def __init__(self,account_no,account_pas):
        self.account_no=account_no
        self.__account_pas=account_pas

    def change(self):
        print("The password is : ",self.__account_pas)

    def __hello(self):
        print("Hello")

    def p(self):
        self.__hello()    

b1=Bank(1234,"abcd")
print(b1.account_no)
# print(b1.account_pas)#-->AS it is private so it will not be printed
# b1.hello()#-->It is not printed because it is private
b1.p()

##-------------------------------INHERITANCE----------------------------------------------##
#-->THere are three types of inheritance 
#-->single level inheritance
##-->Multiple inheritance
#-->Multilevel inheritance

#-->Super method: It is a special method that is used to access the methods of the parent class
class Car:
    
    def __init__(self,brek,clutch,race):
        self.brek=brek
        self.clutch=clutch
        self.race=race
    def start(self):
        print('THe car is started')
 
class Toyota(Car):#-->Single Inheritance
    def __init__(self,name):
        self.name=name

class Fortuner(Toyota):
    def __init__(self, milage):
        self.milage=milage
        super().start()
        

c1=Fortuner(1200)
# c1.start()
# c1.getinfo()

    


