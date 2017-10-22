nota100=0; nota50=0; nota20=0; nota10=0; nota5=0; nota2=0; moeda100=0; moeda50=0; moeda25=0; moeda10=0; moeda5=0; moeda1=0

a=float(input())
a+=0.00000000001

if(a >= 100):
  nota100=a/100
  nota100=int(nota100)
  a=a%100
  
if(a >= 50):
  nota50=a/50
  nota50=int(nota50)
  a=a%50
  
if(a >= 20):
  nota20=a/20
  nota20=int(nota20)
  a=a%20
  
if(a >= 10):
  nota10=a/10
  nota10=int(nota10)
  a=a%10
  
if(a >= 5):
  nota5=a/5
  nota5=int(nota5)
  a=a%5
  
if(a >= 2):
  nota2=a/2
  nota2=int(nota2)
  a=a%2
  
  
  
if(a >= 1):
  moeda100=int(a)
  a=a%1

if(a >= 0.5):
  moeda50=a/0.5
  moeda50=int(moeda50)
  a=a%0.50

if(a >= 0.25):
  moeda25=a/0.25
  moeda25=int(moeda25)
  a=a%0.25

if(a >= 0.1):
  moeda10=a/0.1
  moeda10=int(moeda10)
  a=a%0.1
  
if(a >= 0.05):
  moeda5=a/0.05
  moeda5=int(moeda5)
  a=a%0.05
  
if(a >= 0.01):
  moeda1=a/0.01
  moeda1=int(moeda1)
  a=a%0.01
  
print("NOTAS:")
print(nota100,"nota(s) de R$ 100.00")
print(nota50,"nota(s) de R$ 50.00")
print(nota20,"nota(s) de R$ 20.00")
print(nota10,"nota(s) de R$ 10.00")
print(nota5,"nota(s) de R$ 5.00")
print(nota2,"nota(s) de R$ 2.00")

print("MOEDAS:")
print(moeda100,"moeda(s) de R$ 1.00")
print(moeda50,"moeda(s) de R$ 0.50")
print(moeda25,"moeda(s) de R$ 0.25")
print(moeda10,"moeda(s) de R$ 0.10")
print(moeda5,"moeda(s) de R$ 0.05")
print(moeda1,"moeda(s) de R$ 0.01")
