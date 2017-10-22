O=str(input())
matriz=[]
matrizAcima=[]

for i in range(144):
    N=float(input())
    matriz+=[N]

for i in range(10):
    matrizAcima+=(matriz[(1+(12*i)+i):(12+(12*i))])

matrizAcima.append(matriz[131])
map(float,list(matrizAcima))


soma=sum(matrizAcima)

if(O=="S"):
    print("%.1f"%soma)

if(O=="M"):
    print("%.1f"%(soma/66))
