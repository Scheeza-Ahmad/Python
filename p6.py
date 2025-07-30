##----------------------AVERAGE OF 3 NUMBERS-----------------------##
def cal_average(a,b,c):
    avg=(a+b+c)/3
    print("The average of 3 numbers is : ",avg)
    return avg

cal_average(1,2,3)

##--------------------Print length of a function-------------------##
def cal_length(list):
    l=len(list)
    print("The length of the list is : ",l)
    return l

vegies=["carrot","onion","garlic"]
cal_length(vegies)

##--------------------Print list in single line-------------------##

def cal_length(list):
    for item in list:
     print(item,end=" ")
    return list

vegies=["carrot","onion","garlic"]
cal_length(vegies)

##-------------------Find factorial of n--------------------------##
n=5
def cal_factorial(n):
    fact=1
    for val in range(1,n+1):
       fact*=val
    print("\nThe factorial of the number is : ",fact)   

cal_factorial(5)

##-----------Calculate the sum of first n natural numbers----------##
def cal_sum_natural(n):
   if n == 0:
      return 0
   
   sum=n+cal_sum_natural(n-1)
   return sum


result=cal_sum_natural(5)
print(result) 

##-----Write a recursive function to print all the elements of the list--------##
listt=[1,2,3,4,5,6]
