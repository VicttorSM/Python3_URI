cont=0; contN=1

lista=list(map(int,input().split()))
A=lista[0]
while True:
    if(lista[contN]>0):
        N=lista[contN]
        break
    contN+=1

    
for i in range(N):
    cont+=A
    A+=1
print(cont)
