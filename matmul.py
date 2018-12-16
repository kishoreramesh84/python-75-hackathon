list1=[[0 for i in range(0,3)] for j in range(0,3)]
print(list1)
list2=[[0 for i in range(0,3)]for j in range(0,3)]
print(list2)
print("Enter the element for matrix A:")
for i in range(0,3):
    for j in range(0,3):
        list1[i][j]=int(input("enter :"))
print(list1)
print("Enter the element for Matrix B:")
for i in range(0,3):
    for j in range(0,3):
        list2[i][j]=int(input("enter:"))
print(list2)
print("Multiplication:")
list3=[[0 for i in range(0,3)]for j in range(0,3)]
for i in range(0,3):
    for j in range(0,3):
        list3[i][j]=0
        for k in range(0,3):
            list3[i][j]+=list1[i][k]*list2[k][j]
print(list3)
