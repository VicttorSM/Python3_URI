contY=1; contX=0

X,Y=input().split()
X=int(X)
Y=int(Y)


while(contY<=Y):
    if(contX==X-1):
        print(contY)
        contX=0
        contY+=1
    else:
        print(contY,end=" ")
        contY+=1
        contX+=1
