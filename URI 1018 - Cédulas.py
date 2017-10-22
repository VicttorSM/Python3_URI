nota100=0; nota50=0; nota20=0; nota10=0; nota5=0; nota2=0; nota1=0

inicial=int(input())

a=inicial

if(inicial >= 100):
  nota100=inicial/100
  nota100=int(nota100)
  a=inicial%100
  
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
  nota1=a/1
  nota1=int(nota1)
  a=a%1
  
print(inicial)
print(nota100,"nota(s) de R$ 100,00")
print(nota50,"nota(s) de R$ 50,00")
print(nota20,"nota(s) de R$ 20,00")
print(nota10,"nota(s) de R$ 10,00")
print(nota5,"nota(s) de R$ 5,00")
print(nota2,"nota(s) de R$ 2,00")
print(nota1,"nota(s) de R$ 1,00")
