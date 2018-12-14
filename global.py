print("Global Scope Variable demo!!")
g=34
print("The value of g outside the function",g)
def globaldemo():
    global g #'global' keyword is used to make a variable as global scope
    g=67 #Once the value is changed in or out side the function the original value is also changed
    print("The value of g inside the function",g)
globaldemo()
print("The value of g after the function call",g)
    
