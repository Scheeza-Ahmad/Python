# ##----------------------------LOOPS---------------------------##
## Agar kisi data tyoe pa triverse karna hai to for loop sa karain ga like in tuple or list
## Agar iterator par kam karna hai yani koi variable hai jis pa hum kaam kar raha hai aur usa iterate karn ahia aur uski koi stopping condition hai to phir hum while loop use karta hai

# ##----------------------------WHILE LOOP-----------------------##
# i=1
# while i<=10:
#     print("Hello world")
#     i+=1

# #-->Break 
# j=1
# while j<=10:
#     print("HI")
#     if(j==5):
#         break

#     j+=1    

# #-->Continue-->Here the value is skipped and it moves to the next iteration
# k=1
# while k<=10:
#     if(k==5):
#         k+=1
#         continue
#     print(k)

#     k+=1    

# ##-------------------------FOR LOOP--------------------------##
# #-->It is used for sequential traversal like in the strings and tuples etc
# #-->for variable in list_name:-->yahan par automatically aik aik kar ka list ka sara elements ata jain ga 

# l1=[1,2,3,9,56,43]
# for value in l1:
#     print(value)

# fruits=["Apple","mango","grapes","oranges"]
# for value in fruits:
#     print(value)


# #-->else:
# #-->Agar hum koi aesa kaam karna chahta hai jo sirf tab ho jab ka loop end tak jai to hum else main woh kaam likhta hain
# #-->Agar break ho gaya tha darmayan main kaheen loop to phir else wali condition nahi work kara gi

# numberss=(21,23,45,67,7,8,99,98)
# for values in numberss:
#     print(values)
# else:
#     print("The loop is executed completely")

# number=(21,23,45,67,7,8,99,98)
# for val in number:
#     if val == 45:
#         print("found")
#         break
#     print(val)

# else:
#     print("The loop is executed completely")

# ##-----------------------------RANGE-------------------------##
# #range returns a sequence that starts from zero by default and increments 1 by default and ennding cindition is always given
# #range(starting_value,ending_value,step)-->step means ka value ko kitna increment karna hai

# for i in range(5):#->(end)
#     print("The numbers from 1-5 are : ",i)

# for j in range(1,10):#->(start,end)
#     print("The numbers from 1-10 are : ",j)

# for k in range(1,10,2):#->(start,end,step)
#     print("The numbers from 1-10 with a gap of 2 are : ",k)

# ##--------------------------PASS STATEMENT---------------------##
# # It is used when we are printing an empty 
# for o in range(5):
#     pass

# print("Loop is empty")

# #->It can also be used in if_else statement
# no=10
# if no>=5:
#     pass
# print("If worked successfully")

