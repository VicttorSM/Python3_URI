contPessoas=0; contIdade=0


while True:
    N=int(input())
    if(N<0):
        break
    contPessoas+=1
    contIdade+=N
print("%.2f"%(contIdade/contPessoas))
