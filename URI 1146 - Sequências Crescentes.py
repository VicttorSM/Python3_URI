N=1
while True:
    X=int(input())
    if(X==0):
        break
    while(N<=X):
        if(N<X):
            print(N,end=" ")
        else:
            print(N)
        N+=1
    N=1
