contPositivo = 0; contNumero = 0
for i in range(6):
    A=float(input())

    if(A>0):
        contPositivo += 1
        contNumero += A

print(contPositivo,"valores positivos")
print("%.1f"%(contNumero/contPositivo))
