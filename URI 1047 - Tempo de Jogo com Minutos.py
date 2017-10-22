inicialHoras,inicialMinutos,finalHoras,finalMinutos=input().split()
inicialHoras = int(inicialHoras)
inicialMinutos = int(inicialMinutos)
finalHoras = int(finalHoras)
finalMinutos = int(finalMinutos)

if(inicialHoras >= finalHoras):
    horas = (24-inicialHoras)+ finalHoras
else:
    horas = finalHoras - inicialHoras

if(inicialMinutos > finalMinutos):
    minutos = 60 - (inicialMinutos - finalMinutos)
    horas -= 1
if(inicialMinutos < finalMinutos):
    minutos = finalMinutos - inicialMinutos
    if(horas==24):
        horas=0
if(inicialMinutos == finalMinutos):
    minutos = 0
    
print("O JOGO DUROU",horas,"HORA(S) E",minutos,"MINUTO(S)")
