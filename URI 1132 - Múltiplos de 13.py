cont=0

X=int(input())
Y=int(input())
lista=[X,Y]
lista.sort()
X=lista[0]
Y=lista[1]

while (X<=Y):
    if(X%13!=0):
        cont+=X
    X+=1
print(cont)
