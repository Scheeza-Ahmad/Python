##-----------------------FUNCTIONS--------------------------##
#-->Block of statement that perfor a specific function

#-->function definition
def cal_sum(a,b):#-->parameters
    sum=a+b
    print(sum)
    return sum

#-->function call
cal_sum(1,2)#-->arguments
cal_sum(10,2)
cal_sum(11,12)

#-->function that dont take any input and dont print any output
def print_hello():
    print("Hello World")

print_hello()

#-->Default parameters
def cal_prod(a=1,b=2):
    product=a*b
    print("The product of the two numbers is : ",product)
    return product

cal_prod()

#-->The default arguments always start from end
def cal_prod(a,b=2):
    product=a*b
    print("The product of the two numbers is : ",product)
    return product

cal_prod(2)

##---------------------------RECURSION-----------------------##
#->Agar hum aik function ka andar usi function ko bar bar call karta rahain tab tak ka jab tak hamari condition false na ho jai

def show(n):
    if(n==0):#-->Base case that decides ka yahan recursion rukni chahiya ya nhi
        return #-->The empty return is used to return the control
    print(n)
    show(n-1)

show(5)    

#call stack-->agar aik function ka upper dosra call ho aur dosra ka upper tesra isa hum kehta hai call stack
n=5
def cal_factorial(n):
    if(n==0 or n==1):
        return 1
    
    return n*cal_factorial(n-1)
    
print(cal_factorial(5))  

