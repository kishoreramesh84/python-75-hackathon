print("Basic operation in list")
list1=[1,2,"ram",3.0,"string",5]
print(list1)
#basic operations
print("1.Append")
list1.append("vijay")#Append function is used to add element at the end of the list
print(list1)
list2=[34,44]
list2.extend(list1)#Extend function is used to a list with another list
print("2.Extend")
print(list2)
print("3.Reverse")
list2.reverse()#It reverses the order
print(list2)
list3=["ram",2,"ram",4,6,2,2]
print("4.Count")
print("Given list:",list3,end='\n')
print("Count of 2:",list3.count(2))#Count function return how many times the element is repeated in a list
print("Count of ram:",list3.count("ram"))
print("5.Remove")
list3.remove("ram")#It is used to remove a specific element in a list
print(list3)
print("6.Copy")
list3=list2.copy()#It copies the list2 element to list3
print(list3)
print("7.Length")#It returns the length of the given list
print(len(list3))
print("8.Index")#Index returns the index of the specific element
print("Index of 5",list3.index(5))
print("9.Clear")
list3.clear()#It clears every element in a list
print(list3)
