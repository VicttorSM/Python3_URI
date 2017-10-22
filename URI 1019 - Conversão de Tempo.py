horas=0; minutos=0; segundos=0

inicial=int(input())

a=inicial

if(inicial >= 3600):
  horas=inicial/3600
  horas=int(horas)
  a=inicial%3600
  
if(a >= 60):
  minutos=a/60
  minutos=int(minutos)
  a=a%60
  
if(a >= 1):
  segundos=a
  segundos=int(segundos)
  
print("%i:%i:%i"%(horas,minutos,segundos))
