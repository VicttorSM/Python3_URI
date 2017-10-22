ano=0; mes=0; dia=0

inicial=int(input())

a=inicial

if(inicial >= 365):
  ano=inicial/365
  ano=int(ano)
  a=inicial%365
  
if(a >= 30):
  mes=a/30
  mes=int(mes)
  a=a%30
  
if(a >= 1):
  dia=a
  dia=int(dia)
  
print(ano,"ano(s)")
print(mes,"mes(es)")
print(dia,"dia(s)")
