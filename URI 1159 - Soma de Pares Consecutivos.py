contPar=0; soma=0

while True:
    X=int(input())
    if(X==0):
        break
    while(contPar<5):
        if(X%2==0):
            contPar+=1
            soma+=X
        X+=1
    print(soma)
    soma=0
    contPar=0
