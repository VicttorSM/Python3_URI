while True:
    A=float(input())
    while(A<0 or A>10):
        print("nota invalida")
        A=float(input())
    B=float(input())
    while(B<0 or B>10):
        print("nota invalida")
        B=float(input())
    print("media = %.2f"%((A+B)/2))
    print("novo calculo (1-sim 2-nao)")
    novo=int(input())
    while(novo<1 or novo>2):
        print("novo calculo (1-sim 2-nao)")
        novo=int(input())
    if(novo==2):
        break
