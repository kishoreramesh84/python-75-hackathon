print("Reading operation from a file")
f2=open("newfile2.txt","w")
f2.write(" Hi! there\n")
f2.write("My python demo file\n")
f2.write("Thank u")
f2.close()
f3=open("newfile2.txt","r+")
print("Method 1:")
for l in f3: #Method 1 reading file using loops
    print(l,end=" ")
f3.seek(0) #seek is used to place a pointer to a specific location
print("\nMethod 2:")
print(f3.read(10))#Method 2 it reads 10 character from file
f3.seek(0)
print("Method 3:")
print(f3.readlines())#Method 3 it prints the text in a list
f3.close()
