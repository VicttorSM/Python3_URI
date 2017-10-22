soma=0; contX=1

N=int(input())
for i in range(N):
    X=int(input())
    while(contX<=X):
        if(X%contX==0):
            soma+=contX
        contX+=1
    if(soma==X+1):
        print(X,"eh primo")
    else:
        print(X,"nao eh primo")
        
    soma=0
    contX=1
