while True:
    X,Y=input().split()
    X=int(X)
    Y=int(Y)
    if(X==0 or Y==0):
        break
    if(Y>0):
        if(X>0):
            print("primeiro")
        if(X<0):
            print("segundo")
    if(Y<0):
        if(X<0):
            print("terceiro")
        if(X>0):
            print("quarto")
