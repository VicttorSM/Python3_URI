N=int(input())
for i in range(N):
    X=int(input())
    if(X==0):
        print("NULL")
    else:
        if(X%2==0):
            parImpar=str("EVEN")
        else:
            parImpar=str("ODD")
        if(X>0):
            positivoNegativo=str("POSITIVE")
        else:
            positivoNegativo=str("NEGATIVE")
            
        print(parImpar,positivoNegativo)
