contAlcool=0; contGasolina=0; contDiesel=0

while True:
    N=int(input())
    while(N<1 or N>4):
        N=int(input())
    if(N==1):
        contAlcool+=1
    if(N==2):
        contGasolina+=1
    if(N==3):
        contDiesel+=1
    if(N==4):
        break
print("MUITO OBRIGADO")
print("Alcool:",contAlcool)
print("Gasolina:",contGasolina)
print("Diesel:",contDiesel)
