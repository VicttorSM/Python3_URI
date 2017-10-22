contX=1; soma=0

N=int(input())
for i in range(N):
    X=int(input())
    while(contX<X):
        if(X%contX==0):
            soma+=contX
        contX+=1
    if(soma==X):
        print(X,"eh perfeito")
    else:
        print(X,"nao eh perfeito")
    
    soma=0
    contX=1
