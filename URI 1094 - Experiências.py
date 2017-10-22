contCoelho=0; contRato=0; contSapo=0

N=int(input())
for i in range(N):
    quantia,tipo=input().split()
    quantia=int(quantia)
    tipo=str(tipo)
    if(tipo=="C"):
        contCoelho+=quantia
    if(tipo=="R"):
        contRato+=quantia
    if(tipo=="S"):
        contSapo+=quantia

total=contCoelho+contRato+contSapo
print("Total:",total,"cobaias")
print("Total de coelhos:",contCoelho)
print("Total de ratos:",contRato)
print("Total de sapos:",contSapo)
print("Percentual de coelhos: %.2f %%"%((contCoelho*100)/total))
print("Percentual de ratos: %.2f %%"%((contRato*100)/total))
print("Percentual de sapos: %.2f %%"%((contSapo*100)/total))
