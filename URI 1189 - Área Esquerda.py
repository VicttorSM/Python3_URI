O=str(input())
matriz=[]
matrizAcima=[]

for i in range(144):
    N=float(input())
    matriz+=[N]

for i in range(5):
    matrizAcima+=(matriz[(12+(i*12)):(13+(i*12)+i)])

for i in range(5):
    matrizAcima+=(matriz[(12+(5*12)+(12*i)):(12+(5*12)+(12*i)+(+5-i))])


map(float,list(matrizAcima))


soma=sum(matrizAcima)

if(O=="S"):
    print("%.1f"%soma)

if(O=="M"):
    print("%.1f"%(soma/30))
