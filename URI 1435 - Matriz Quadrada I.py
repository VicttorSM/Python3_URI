linha=0; coluna=0

while True:
    N=int(input())
    if(N==0):
        break
    for i in range(N):
        linha+=1
        for i in range(N):
            coluna+=1
            if(coluna==N):
                print("1")
                coluna=0
                break
            
            elif(coluna >N/2):
                print(N-coluna,end=" ")
            elif(coluna==linha):
                print(coluna,end=" ")

        if(linha==N):
            linha=0
            break
            
