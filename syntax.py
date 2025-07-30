##--------------------------LIST---------------------------------##
list=[1,2,3,4,5]
##--------------------------TUPLE--------------------------------##
tuple=(14,67,89,54,2)
##--------------------------DICTIONARY---------------------------##
dictionary={
    "key":"value",
    "rollno":2
}
print(dictionary)
##-------------------------SET-----------------------------------##
set={2,4,67}
print(set)
##------------------------LOOPS----------------------------------##
for value in list:
    print(value)

for value in tuple:
    print(value)

i=1
while (i<5):
    print(i)
    i+=1

##-------------------------RANGE---------------------------------##
for value in range(5):#-->stopping value
    print(value)

for value in range(5,10):#-->(starting value,stopping value)
    print(value)

for value in range(5,10,2):#-->(starting value,stopping value,step)
    print(value)    

##-----------------------FUNCTION--------------------------------##
def cal_sum(a,b):
    sum=a+b
    print(sum)
    return sum
cal_sum(1,2)    

##----------------------RECURSION--------------------------------##
def show(n):
    if(n==0):#-->Base case that decides ka yahan recursion rukni chahiya ya nhi
        return #-->The empty return is used to return the control
    print(n)
    show(n-1)

show(5)    
