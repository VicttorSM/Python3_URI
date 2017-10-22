X=int(input())
Y=int(input())
lista=[X,Y]
lista.sort()
X=lista[0]
Y=lista[1]

X+=1
while(X<Y):
    if(X%5==2 or X%5==3):
        print(X)
    X+=1
