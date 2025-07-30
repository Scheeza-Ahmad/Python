##--------------------------------CLASS----------------------------##
#-->The name of the class should begin with the capital letter
# class Student:
#     name="schezza"

# s1=Student()
# print(s1.name)

##--------------------------------CONSTRUCTOR----------------------##
# All classes have a function that is called init function that is executed when the object is initiated
class Student:
    n="schezza" #-->class attribute
    #-->Default constructor
    def __init__(self):
         pass
    #->parametrized constructor
    def __init__(self,name,marks):#-->The self here points towards the object of the class Student
                         #-->Here a is a variable  
                        
         self.name=name     #-->Constructor ka variables ko hum attributes kehta hain
         self.marks=marks   #-->instance attribute
         print("Hello there")
    #-->Method     
    def getmarks(self):
        return self.marks     

s1=Student("Ayesha",35)
print(s1.name,s1.getmarks())#-->calling of the instance attribute

# Student.n() #-->Calling of the class attribute
##------------------------------ATTRIBUTES--------------------------##
#It has two types
#-->CLASS ATTRIBUTES-->That is common for all the objects of the class
#-->INSTANCE ATTRIBUTES-->That is different on the base of the object

##-----------------------------METHODS--------------------------##
#-->class is a combination of attributes and method
#-->Function that belong to objects

#------------------------------STATIC METHOD------------------##
##-->Method that use the self parameters
class Name:
     @staticmethod #--->It is a decorator
     def getname():
          print("The name is : Scheeza")
n=Name
n.getname()          

##---------------------------ABSTRACTION--------------------------##
#-->Hiding the implementation details in a class and only showing essential features to the user
class Car:
     def __init__(self):
          self.braek=False
          self.clutch=False
          self.acc=False

     def start(self):
           self.clutch=True
           self.acc=True
           print("Car is started")
           
c1=Car()
c1.start()
#-->iss example main start sa end tak sara program back end pa kaam kar raha hai class main magar print consolve pa sirf car started ho raha hai to yeh hai encapsulation

##-----------------------ENCAPSULATION---------------------------##
#-->Wrapping data and function into a single unit(object)


