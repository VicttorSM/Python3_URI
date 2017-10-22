salario = float(input())

if(0 <= salario <= 400):
    reajuste = 15
if(400 < salario <= 800):
    reajuste = 12
if(800 < salario <= 1200):
    reajuste = 10
if(1200 < salario <= 2000):
    reajuste = 7
if(salario > 2000):
    reajuste = 4

reajusteGanho = salario*(reajuste/100)
novoSalario = salario + reajusteGanho

print("Novo salario: %.2f"%novoSalario)
print("Reajuste ganho: %.2f"%reajusteGanho)
print("Em percentual:",reajuste,"%")
