O=str(input())
matriz=[]
matrizAbaixo=[]

for i in range(144):
    N=float(input())
    matriz+=[N]


for i in range(12):
    matrizAbaixo+=(matriz[((i*12)):((i*12)+i)])

map(float,list(matrizAbaixo))

soma=sum(matrizAbaixo)

if(O=="S"):
    print("%.1f"%soma)

if(O=="M"):
    print("%.1f"%(soma/66))
