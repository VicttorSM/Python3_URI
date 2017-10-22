N=int(input())
lista=[]
temporária=list(map(int,input().split()))

for i in range(N):
    lista+=temporária
print("Menor valor:",min(lista))
print("Posicao:",lista.index(min(lista)))
