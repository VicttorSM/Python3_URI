dias=0; horas=0; minutos=0; segundos=0

di=input()
di=di[4:]
di=int(di)
hi,mi,si=input().split(" : ")
hi=int(hi)
mi=int(mi)
si=int(si)

df=input()
df=df[4:]
df=int(df)
hf,mf,sf=input().split(" : ")
hf=int(hf)
mf=int(mf)
sf=int(sf)

hi+=di*24
mi+=hi*60
si+=mi*60

hf+=df*24
mf+=hf*60
sf+=mf*60

segundos=sf-si

if(segundos>0):
    while(segundos>=(60*60*24)):
        dias+=1
        segundos-=(60*60*24)
    while(segundos>=(60*60)):
        horas+=1
        segundos-=(60*60)
    while(segundos>=60):
        minutos+=1
        segundos-=60

    print(dias,"dia(s)")
    print(horas,"hora(s)")
    print(minutos,"minuto(s)")
    print(segundos,"segundo(s)")
