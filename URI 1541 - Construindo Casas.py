while True:
    var = list(map(int,input().split()))
    if((len(var) == 1) and (var[0] == 0)):
        break
    if(len(var) >= 3):
        A,B,C = var[0],var[1],var[2]
        tamanhoTotal = A*B*(C/100)
        X = (tamanhoTotal**(1/2))/(C/100)
        X = int(X)
        print(X)
