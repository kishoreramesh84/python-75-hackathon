a=(1,3,5)
print("tuple  :",a)
print("values of a tuple can't be change once it's created")
print("but it can be done by casting it as a list and recasting back to tuple after adding the element")
a=list(a)
print("a as list  :",a)
a.append(6)
print("list a after appending 6 ;",a)
a=tuple(a)
print("tuple a :",a)