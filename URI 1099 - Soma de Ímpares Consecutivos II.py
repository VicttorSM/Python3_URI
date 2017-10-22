contImpar=0

N=int(input())

for i in range(N):
    X,Y=input().split()
    X=int(X)
    Y=int(Y)

    lista=[X,Y]
    lista.sort(reverse=True)
    X=lista[0]
    Y=lista[1]

    if(Y%2==0):
        A=Y+1
    else:
        A=Y+2
    while (A<X):
        contImpar += A
        A += 2
    print(contImpar)
    contImpar=0
