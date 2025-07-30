##-----------------------DICTIONARY-------------------------##
# It consists of the key:value every key has a specific value 
# key can be anything that is unmutable like integer string float or a tuple
# value can be either be a string float integer list or tuple. It can be mutable

# SYNTAX:
# dictionary_name={
#     key:value,
# }

#->Dictionary is mutable and we cannot use the key for more then once 
student={
"name":"Scheeza Ahmad",
"gpa":3.63,
"cgpa":3.49,
"subjects":["mvc","oop","discrete","coal"],
"topics":("dictionary","sets")
}
print("The dictionary of student is : ",student)
print("The name of the student is : ",student["name"])
print("The cgpa of the student is : ",student["cgpa"])

# -->Mutation
student["name"]="ayesha"
print("The name of the student is : ",student["name"])

#-->appendable
student["isadult"]=True
print("The info of student is : ",student)

#-->overwrite
student["name"]="amna"
print("The name of the student is : ",student["name"])

#-->Empty dictionary
empty={}
print("The empty dictionary is : ",empty)

#-->Nested dictionary
#->agar dictionary ka andar kisi key ki aga hum dictionary bana dain to isa kehta hain nested dictionary
students={
"name":"Scheeza Ahmad",
"gpa":3.63,
"cgpa":3.49,
"subjects":{
    "english":90,
    "urdu":78,
    "maths":100
},
"topics":("dictionary","sets")
}
#->accessing the whole dictionary of students
print("The keys and the values of the students nested dictionary are : ",students)
#->accessing the nested dictionary
print("The key and attributes of the subject is : ",students["subjects"])
#->accessing the elements of the nested dictionary
print("The key and attributes of the urdu is : ",students["subjects"]["urdu"])

##----------------------METHODS OF THE DICTIONARY----------------------##

#->printing keys-->It prints only parent keys nested keys are not printed 
print("The keys of the students dictionary are : ",students.keys())

#->printing values-->It prints the values of the parent
print("The values of the student dictionary are : ",students.values())

#->It is used to delete the specific item
students.__delitem__("topics")
print("The dictionary after deleting the items are : ",students)

#->Calculating the length of the keys->it only calculaes the length of the parent
print("The length of the keys are : ",len(list(students.keys())))

#->getting teh keys and values in a tuple and type casted it with list which is completely optional
print("The key and the values in the tuple are : ",list(students.items()))
l=list(students.items())

#->we can also access each tuple individually
print("The first tuple is : ",l[0])

#->printing the value of a specific key-->The benifit is that if the error is thrown in future then the program doesnt stops
print("It prints the value of the name : ",students.get("name"))

#->updating a dictionary
#->we can either pass a new dictionary or we can pass the kay and value in the curly braces
students.update({"age":20})
print(students)

#->Adding new dictionary to the previous dictionary
new={
    "city":"Lahore",
    "Area":"johar town"
}
students.update(new)
print(students)
