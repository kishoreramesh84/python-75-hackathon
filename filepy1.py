print("FILE HANDLING IN PYTHON!!")
f1=open("newfile1.txt","w") #'w' is used for writing into a file
f1.write("Python demo file\n")
f1.write("Hi! everyone\n")
f1.write("Thank u")
f1.close()
f1=open("newfile1.txt","r")#'r' is used for reading from a file
s=f1.read()
print(s)
f1.close()
    
    
