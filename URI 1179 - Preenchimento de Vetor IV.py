par=[]; impar=[]; contPar=0; contImpar=0
for i in range(15):
    N=int(input())
    if(N%2!=0):
        impar+=[N]
        contImpar+=1
        if(contImpar==5):
            for i in range(5):
                print("impar[%i] = %i"%(i,impar[i]))
            impar=[]
            contImpar=0
    if(N%2==0):
        par+=[N]
        contPar+=1
        if(contPar==5):
            for i in range(5):
                print("par[%i] = %i"%(i,par[i]))
            par=[]
            contPar=0

for i in range(contImpar):
    print("impar[%i] = %i"%(i,impar[i]))

for i in range(contPar):
    print("par[%i] = %i"%(i,par[i]))
