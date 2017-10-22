N=int(input())
for i in range(N):
    X,Y=input().split()
    X=int(X)
    Y=int(Y)
    if(Y==0):
        print("divisão impossivel")
    else:
        print(X/Y)
