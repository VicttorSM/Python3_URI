contInter=0; contGremio=0; contEmpate=0; contGrenais=0

while True:
    inter,gremio=input().split()
    inter=int(inter)
    gremio=int(gremio)
    
    if(inter>gremio):
        contInter+=1
    elif(gremio>inter):
        contGremio+=1
    else:
        contEmpate+=1
    contGrenais+=1
    
    print("Novo grenal (1-sim 2-nao)")
    novo=int(input())
    if(novo!=1):
        break
    
print(contGrenais,"grenais")
print("Inter:%i"%contInter)
print("Gremio:%i"%contGremio)
print("Empates:%i"%contEmpate)
if(contInter>contGremio):
    print("Inter venceu mais")
elif(contGremio>contInter):
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
