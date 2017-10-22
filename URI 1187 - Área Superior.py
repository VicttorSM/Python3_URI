O=str(input())
matriz=[]
matrizAcima=[]

for i in range(144):
    N=float(input())
    matriz+=[N]

for i in range(5):
    matrizAcima+=(matriz[((1+i)+(12*i)):(11+(12*i)-i)])



map(float,list(matrizAcima))


soma=sum(matrizAcima)

if(O=="S"):
    print("%.1f"%soma)

if(O=="M"):
    print("%.1f"%(soma/30))
