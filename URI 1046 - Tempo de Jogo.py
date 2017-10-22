inicial,final=input().split()
inicial=int(inicial)
final=int(final)

if(0<=inicial<=24 and 0<=final<=24):
    if(inicial >= final):
        horas = (24-inicial)+final
    else:
        horas = final - inicial
    print("O JOGO DUROU",horas,"HORA(S)")
