N=int(input())
for i in range(N):
    contDias=0
    C=float(input())
    while(C>1):
        C/=2
        contDias+=1

    print(contDias,"dias")
