O=str(input())
matriz=[]
matrizAbaixo=[]

for i in range(144):
    N=float(input())
    matriz+=[N]


for i in range(6):
    matrizAbaixo+=(matriz[(12+((12*6)+i*12)-(6+i)):((12*6)+(i*12)+(6+i))])


map(float,list(matrizAbaixo))


soma=sum(matrizAbaixo)

if(O=="S"):
    print("%.1f"%soma)

if(O=="M"):
    print("%.1f"%(soma/30))
