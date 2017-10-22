B=0; C=1

N=int(input())
for i in range(N):
    if(i+1<=2):
        print(i,end=" ")
    else:
        A=B
        B=C
        C=A+B
        if(i==N-1):
            print(C)
        else:
            print(C, end=" ")
