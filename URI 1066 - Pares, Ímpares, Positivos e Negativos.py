contPar = 0; contImpar = 0; contPositivo = 0; contNegativo = 0

for i in range(5):
    A=int(input())

    if(A%2==0):
        contPar += 1
    else:
        contImpar += 1
    if(A>0):
        contPositivo += 1
    if(A<0):
        contNegativo += 1

print(contPar,"valor(es) par(es)")
print(contImpar,"valor(es) impar(es)")
print(contPositivo,"valor(es) positivo(s)")
print(contNegativo,"valor(es) negativo(s)")
