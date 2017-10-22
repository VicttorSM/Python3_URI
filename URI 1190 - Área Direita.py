O=str(input())
matriz=[]
matrizAcima=[]

for i in range(144):
    N=float(input())
    matriz+=[N]

for i in range(6):
    matrizAcima+=(matriz[(12+(i*12)-i):(12+(12*i))])


for i in range(5):
    matrizAcima+=(matriz[(12+(6*12)+(i*12)-5+i):(12+(12*6)+(12*i))])


map(float,list(matrizAcima))



soma=sum(matrizAcima)

if(O=="S"):
    print("%.1f"%soma)

if(O=="M"):
    print("%.1f"%(soma/30))
