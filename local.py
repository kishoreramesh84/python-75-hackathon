print("Local scope variable demo!!")
l1=100
def demolocal():
    l1=34#Local variable
    print(l1,"local value inside the function")
demolocal()
print("outside the function",l1)
