soma=0

while True:
    soma=0
    M,N=input().split()
    M=int(M)
    N=int(N)
    lista=[M,N]
    lista.sort()
    if(M<=0 or N<=0):
        break
    else:
        while(lista[0]<=lista[1]):
            print(lista[0],end=" ")
            soma+=lista[0]
            lista[0]+=1
        print("Sum=%i"%soma)
