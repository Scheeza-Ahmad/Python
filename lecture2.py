##--------------STRINGS---------------##


#-->Ways to write the string
s1="I am learning python."
s1='I am learning python.'
s1="""I am learning python."""

#-->escape sequence characters
#There are two escape sequence characters \n->(for moving to the next line) and \t->(for tab space)

str1="My name is scheeza.\nMy age is 20 years." 
str2="My name is scheeza.\tMy age is 20 years." 
print("The string after the next line space is : ",str1)
print("The string after the tab space is : ",str2)

#-->Concatenation-->Adding the two strings together
str3="Scheeza is a good girl."
str4="Scheeza is healthy."
print("The strng after concatenation is : ",str3+str4)

#-->Length of the string->Space is also counted
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

# -->Indexing-->We can only access different variables in it we cannot manipulate any index
str5="Hello here!!"
print(str5[8])
#str5[0]="@"-->It is invalid

#-->Slicing-->Accessing parts of the string
#Here we pass two index
# SYNTAX:
# str[STARTING_INDEX:ENDING_INDEX]-->Starting index is include but ending index is not included
#str[strting_index:]--->ending index=length of the string
#str[:ending index]-->starting index=0
print("Slicing : ",str5[1:8])
print("Slicing : ",str5[:8])
print("Slicing : ",str5[1:])

#-->Negative indexing
# In python we can also count backwords like from end to zero index in this case we will count last index as -1 and so on
print("Slicing by negative indexing : ",str5[-8:-1])

#-->Functions of strings

#-->str.endswith()--->It checks ka brackets main jo chez di hai uspar string khatam ho rahi hai ya nahi agar ho rahi hai to True warna False
print("Working of the endswith function : ",str5.endswith("!!"))
print("Working of the endswith function : ",str5.endswith("er"))

#-->str.capatilize-->Yeh string ka first alphabet ko capatilize kar daita hai but yeh permanent nhi hota sirf uss time ka liya hota hai
str6="hello guys"
print("After temporary capatilize : ",str6.capitalize())
print(str6)
#->Permanent changes to the string
str6=str6.capitalize()
print("After permanent capatilize : ",str6)

# -->str.replace()-->It replaces the old value with some new 
print("The word after replacement is : ",str6.replace("e","p"))
print("The word after replacement is : ",str6.replace("Hello","Pagal"))

# -->str.find(word)-->It finds the word aur jahan woh first time hota hai uska first index woh return kar daita hai
print("The word is found at index : ",str6.find("l"))
print("The word is found at index : ",str6.find("guys"))

#-->str.count()-->It count the number of occurences
print("The number of occurences of the word is : ",str6.count("l"))


##----------------------CONDITIONAL STATEMENTS----------------------##
#IF ELIF ELSE
light="yellow"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("move")    
else:
    print("sabar karo")