N=int(input())
for i in range(N):
    A,B,C=input().split()
    A=float(A)
    B=float(B)
    C=float(C)
    media=((A*2)+(B*3)+(C*5))/10
    print("%.1f"%media)
