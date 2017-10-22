lista=[]
for i in range(10):
    X=int(input())
    if(X<=0):
        X=1
    lista+=[X]
for i in range(10):
    print("X[%i] = %i"%(i,lista[i]))
