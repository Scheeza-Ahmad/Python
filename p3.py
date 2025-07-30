#------------------------------ASK USER TO ENTER THE MOVIES IN A LIST------------##

movie=[]
mov1=input("Enter your 1st favourite movies : ")
mov2=input("Enter your 2nd favourite movies : ")
mov3=input("Enter your 3rd favourite movies : ")
movie.append(mov1)
movie.append(mov2)
movie.append(mov3)
print(movie)

##--------------------------Check if the list is a palindrome or not--------------##
list=[1,2,3,7,1]
list2=[]
list2=list.copy()
list2.reverse()
if(list==list2):
    print("The two lists are the palindrome of each other")
else:
    print("The two lists are not the paindrome of each other")

#------------------------COUNT THE STUDENTS WITH THE GRADE A IN THE TUPLE----------------##

grade=("A","B","A","A","C","B","F")
print("The students who scored an A grade are : ",grade.count("A"))

##------------------------Sort the tuple -------------------------##
gradee=["A","B","A","A","C","B","F"]
gradee.sort()
print(gradee)