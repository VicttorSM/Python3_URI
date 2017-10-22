C=int(input())
T=str(input())
matriz=[]
soma=0

for i in range(144):
    N=float(input())
    matriz+=[N]

for i in range(12):
    soma+=matriz[C+(i*12)]

if(T=="S"):
    print("%.1f"%soma)

if(T=="M"):
    print("%.1f"%(soma/12))
