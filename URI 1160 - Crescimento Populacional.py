contAnos=0

T=int(input())
for i in range(T):
    PA,PB,G1,G2=input().split()
    PA=int(PA)
    PB=int(PB)
    G1=float(G1)
    G2=float(G2)

    while True:
        PA=int(PA + (PA*(G1/100)))
        PB=int(PB + (PB*(G2/100)))
        contAnos+=1
        if(contAnos>100):
            print("Mais de 1 seculo.")
            contAnos=0
            break
        if(PA>PB):
            print(contAnos,"anos.")
            contAnos=0
            break
