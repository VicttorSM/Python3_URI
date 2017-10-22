A=[]

for i in range(100):
    N=float(input())
    A+=[N]
    if(N%1==0):
        A[i]=int(A[i])
    else:
        A[i]=float(A[i])

for i in range(100):
    if(A[i]<=10):
        print("A[%i] = %.1f"%(i,A[i]))
