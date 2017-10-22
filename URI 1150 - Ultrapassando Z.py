qntd=0; contX=0

X=int(input())
Z=int(input())
while(Z<=X):
    Z=int(input())
    
while(contX<=Z):
    if(qntd==0):
        contX=X
    else:
        X+=1
        contX+=X
    qntd+=1

print(qntd)
