a,qntd1,valor1=input().split()
b,qntd2,valor2=input().split()
qntd1=int(qntd1)
qntd2=int(qntd2)
valor1=float(valor1)
valor2=float(valor2)

total = (qntd1*valor1)+(qntd2*valor2)
print("VALOR A PAGAR: R$ %.2f"%total)
