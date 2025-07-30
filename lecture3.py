# ##-----------------LISTS(mutable datatype)--------------------##
# # A built in data type that is used to store alot of values
# # It is similar to array in c++. But it is different in a way that it is used to store different data types together 
# #The concept of indexing and slicing is also allowed in lists
# #Lists are mutable->we can change the values f the lists

student=["Scheeza",20,"Lahore"]
print("The type of the data type is : ",type(student))

#->mutation
student[0]="Ayesha"
print(student)

#->Slicing
print(student[1:2])

#->Length
print(len(student))

##--------------METHODS IN LISTS-----------------##

marks=[23,89,56,90,12,23,78,99]
print(len(marks))
print("The list after adding the other number is : ",marks.append(9))
print(marks)
print("The list in the descending order is : ",marks.sort(reverse=True))
print(marks)
print("The list in the ascending order is : ",marks.sort())
print(marks)
print("The list in the reverse order is : ",marks.reverse())
print(marks)
marks.insert(1,2)#-->It inserts the specific element at the index marks.insert[index,element]
print("The list after adding a number at a specific index is : ",marks)
#->In string the sorting is done on the basis of the alphabets
marks.remove(23)#-->It removes the value that is tp be removed which comes first
print("The list after removing the specific element is : ",marks)
marks.pop(0)#-->It is used to remove the value from the specific index->marks.pop(index)
print("The list after removing the specific element at the specific index is : ",marks)
print("The number of occurances is : ",marks.count(23))#-->It is used to count the occurance of a specific element
fruits=["mango","apple","banana","orange","lichi"]
fruits.sort()
print("The sorted string list is : ",fruits)

#->The sorting cannot be done on the list that contains both the string and int data types

##--------------------TUPLES(immutable data type)-----------------##
tup=(21,23,78,9,2,98,2,2,2,2)
print("The data type of this is : ",type(tup))

#->Indexing
print(tup[1])
#Manipulation is not allowed in tuples

tup1=()#->Empty tupple
print(tup1)

tup2=(1,)#->If one element is stored then it is written with the comma ahead otherwise it is treated as a integer
print(tup2)

#->Slicing
print(tup[0:2])

print("The index where the value occured for the first time is : ",tup.index(2))#-->It returns the index at which the specific value comes for the first time 

print("The number of times the value occured is : ",tup.count(2))#-->It count the number of times a specific vlue is repeated

