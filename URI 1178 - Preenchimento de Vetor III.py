vetor=[]

X=float(input())
vetor+=[X]
for i in range(100):
    X/=2
    vetor+=[X]
for i in range(100):
    print("N[%i] = %.4f"%(i,vetor[i]))
