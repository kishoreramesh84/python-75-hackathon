def pretopost(pre):
    a=[]
    c=[]
    top=-1
    for i in range(len(pre)):
        if(pre[i]=='+' or pre[i]=='-' or pre[i]=='*' or pre[i]=='/'):
            a.append(pre[i])
            top=top+1
        else:
            c.append(pre[i])
            while(top!=-1 and a[top]=='$'):
                a.pop()
                top=top-1
                c.append(a.pop())
                top=top-1
            a.append('$')
            top=top+1
    postfix=""
    for ex in c:
        postfix=postfix+ex
    print(postfix)    
prefix=input("enter the prefix expression")
pretopost(prefix)
            
