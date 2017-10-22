contImpar=0; soma=0

N=int(input())
for i in range(N):
    X,Y=input().split()
    X=int(X)
    Y=int(Y)
    while(contImpar<Y):
        if(X%2==1):
            contImpar+=1
            soma+=X
        X+=1
    print(soma)
    soma=0
    contImpar=0
