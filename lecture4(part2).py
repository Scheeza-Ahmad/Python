##----------------------SETS---------------------------##
# ->set is a collection of unique and immutable elements
#->set is mutable and elements are immutable
# ->It is a unordered items collection
#->All the values are accepted except lists and dictionary because they both are mutable
#->It ignore the duplicate values
#->length also ignores the duplicate values

collection={1,2,2,2,23,4,"Hello",1.234}
print(collection)
print(len(collection))

#-->EMPTY SET
col=set()
print(col)

#-->Methods of set

#->it is used to add the values in the set
col.add(1)
col.add(3)
col.add("hello")
col.add((2,3,"abc"))
print(col)

#->It is used to remove the values
#col.remove(5)-->It will throw the error as 5 was not present
col.remove("hello")
print(col)

#->it is used to pop the random value
col.pop()
print(col)

#->It is used to claer the set
col.clear()
print(col)

set1={1,2,3,4}
set2={4,5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))


