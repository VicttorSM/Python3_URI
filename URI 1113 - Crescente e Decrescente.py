while True:
    X,Y=input().split()
    X=int(X)
    Y=int(Y)
    if(X>Y):
        print("Decrescente")
    if(X<Y):
        print("Crescente")
    if(X==Y):
        break
