#PYTHON IS A CASE SENSITIVE LANGUAGE IT MEANS THAT IN PYTHON A and a are diiferent
#For commenting the whole code ctrl+/
##-----------PRINT ON CONSOLE--------##

#IF YOU WANT TO PRINT THE THINGS IN DIFFERENT LINES THEN WRITE THE PRINT STATEMENT IN DIFFERENT LINES
print("hello world")
print(1234)
print("Life is amazing")
#IF YOU WANT TO PRINT THE THINGS IN THE SAE LINE THEN USE THE PRINT STATEMENT ONCE AND SEPERATE IT WITH THE HALP OF COMMA
print("Hi my name is scheeza","I am 20 years old")


##--------------VARIABLES-------------##
name="scheeza"
name1='ayesha'
name2='''madam'''
age=20
price=300.3
hobby="discovering herself"
n=name
a=None 
t=True
print(name,age,hobby)
print("My name is : ",n)
print("My other name is : ",name1)
print("My short name is : ",name2)
print("My age is : ",age)
print("My hobby is : ",hobby)
print("My price of dollar is : ",price)

##-----------DATA TYPES -----------##
#Majorly there are 5 data types
#integer
#string
#boolean
#float(True or False)--->They are also reserved word
#None-->reserved word
print("The data types of the variables are : ")
print(type(name))
print(type(age))
print(type(hobby))
print(type(a))
print(type(t))

##-----SUM OF two Numbers ----##

num1=10
num2=8
print("The sum of the two numbers is : ",num1+num2)

##------OPERATORS-------##
n1=10
n2=5

#-->Arithmatic Operators
print("THE ANSWERS OF THE Arithmatic OPERATORS ARE : ")

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1%n2)#-->remainder
print(n1**n2)#-->n1^n2

#-->Relational Operators
print("THE ANSWERS OF THE Relational OPERATORS ARE : ")

print(n1==n2)
print(n1!=n2)
print(n1>=n2)
print(n1<=n2)
print(n1<n2)
print(n1>n2)

#-->Assignment operators
print("THE ANSWERS OF THE ASSIGNMET OPERATORS ARE : ")
r=20
r+=10
print(r)
r-=10
print(r)
r*=2
print(r)
r/=2
print(r)
r%=2
print(r)
v=3
v**=2
print(v)

#-->Logical operators
#not,or,and

#not--->It works on the single operand
print("The answer of he NOT operator is : ",not True)
print(not (n1>n2))

#and or -->It works on two operands

val1=True
val2=False

print("The ans of the AND operator is : ",val1 and val2)
print("The answer of the OR operator is : ",val1 or val2)
print("The answer of the and operation is : ",(n1>n2)and(n1==n2))
print("The answer of the or operation is : ",(n1>n2) or (n1==n2))


##---------TYPE CONVERSION-------##
#->Type conversion is the automatic conversion done by python if one value is float and the oyjer is int and we want to sum to sum it then the answer will be float
#->Type casting is the manual conversion of the variable from one data type to other It is done with the help of different functions

number1=10
number2=6.90
print("The sum after type conversion is : ",number1+number2)

number3=int("2")
print("The sum after type casting is : ",number1+number3)

#number4="scheeza"-->This wll not work because type casting only works when one data fits in the data type 

##-------TAKING INPUT---------##
#When we take input it is always in string so if we want to take integer or float then we type cast it
nameeeee=input("Enter your name : ")
ageee=int(input("Enter your age : "))
markss=float(input("Enter your markss : "))
print("The entered name is : ",nameeeee)
print("The entered age is : ",ageee)
print("The entered marks is : ",markss)
