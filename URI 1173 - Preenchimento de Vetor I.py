contV=0; lista=[]

V=int(input())
for i in range(10):
    if(i==0):
        contV=V
        lista+=[contV]
    else:
        contV*=2
        lista+=[contV]

for i in range(10):
    print("N[%i] = %i"%(i,lista[i]))
    
