def sortdict(di):
    print("ascending order",sorted(di,key=lambda x:di[x]))
    print("descending order",sorted(di,key=lambda x:di[x],reverse=True))
    
d={}
length=int(input("enter the length of the dict"))
for i in range(length):
    key=input("enter the key")
    value=input("enter the value")
    d[key]=value
sortdict(d)    
