def velocidade(n):
    if(n<10):
        return 1
    elif(10<=n<20):
        return 2
    elif(n>=20):
        return 3
while True:
    try:
        lista = []
        L = int(input())
        temp = list(map(int,input().split()))
        for i in range(L):
            lista.append(temp[i])
        nivel = velocidade(max(lista))
        print(nivel)
        
    except EOFError:
        break
