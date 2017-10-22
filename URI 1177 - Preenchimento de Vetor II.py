N=[]; contT=0

T=int(input())
for i in range(1000):
    if(contT==T):
        contT=0
    N+=[contT]
    contT+=1

for i in range(1000):
    print("N[%i] = %i"%(i,N[i]))
