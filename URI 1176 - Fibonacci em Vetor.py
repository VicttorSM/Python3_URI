A=0; B=0; C=1; contN=3; Fib=[]

for i in range(61):
    if(i==0):
        Fib+=[0]
    elif(i==1):
        Fib+=[1]
    else:
        A=B
        B=C
        C=A+B
        Fib+=[C]

T=int(input())
for i in range(T):
    N=int(input())
    print("Fib(%i) = %i"%(N,Fib[N]))
