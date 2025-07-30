# ##-------------------PRINT THE NUMBERS FROM 1-100-------------------##
# i=1
# while i<=100:
#     print(i)
#     i+=1

# ##-------------------PRINT THE NUMBERS FROM 100-1-------------------##
# j=100
# while j>=1:
#     print(j)
#     j-=1

# ##-------------------PRINT THE MULTIPLICATION TABLE OF n---------------##
# k=1
# while k<=10:
#     print(2*k)
#     k+=1

# ##------------------PRINT THE LIST USING LOOP---------------------##
# l1=[2,4,9,16,25,36,49,56,63]
# index=0
# while index<=len(l1):
#     print(l1[index])
#     index+=1

# ##-----------------SEARCH FOR NUMBER X USING LOOP IN TUPLE------------------##
# t1=(32,43,32,9,67,21,90,8,1,2,12,7)
# i=0
# num=32
# while i<=len(t1):
#     if(t1[i]==num):
#         print("Number found successfully!!",i)

#     i+=1

# ##--------------PRINT THE EVEN NUMBERS--------------------------##
# l=1
# while l<=10:
#     if(l%2!=0):
#         l+=1
#         continue
#     else:
#         print(l)

#     l+=1    

# ##---------------PRINT THE ELEMENTS OF THE LIST USING LOOPS--------------##
# listt=[21,23,45,66,77,88,"a",9.76]
# for value in listt:
#     print(value)

# ##--------------Search for the number in a tuple using a loop---------------##
# tuplee=(2,4,5,6,6,9,7,7,7,8)
# count=0
# for val in tuplee:
#     if val==7:
#         print("found")
#         count+=1
#         continue
#     print(val)  
# print("The number of times 7 found is : ",count)

# ##-----------------PRINT NUMBER 1-100 USING RANGE------------##
# for i in range(101):
#     print("The numbers from 1-100 are : ",i)

# ##-----------------PRINT NUMBER 100-1 USING RANGE------------##
# for j in range(100,0,-1):
#     print("The numbers from 100 to 1 are : ",j)

# for k in range(11):
#     print("The table of 2 is : ",2*k)    

# ##--------------sum of first n numbers using while loop-----------------##
# numberadded=int(input("Enter the number : "))
# n=1
# sum=0
# while(n<=numberadded):
#     sum+=n
#     n+=1

# print("The sum of first n numbers is : ",sum)

##------------------------Factorial of first 5 values in list--------------##
numberfact=5
fact=1
for v in range(5,0,-1):
    fact*=v

print(fact)    

