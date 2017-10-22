A=1

N=int(input())
if(1<N<1000):
    while(A<=N):
        print(A,A**2,A**3)
        print(A,(A**2)+1,(A**3)+1)
        A+=1
