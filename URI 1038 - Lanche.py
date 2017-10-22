cod,qntd=input().split()
cod=int(cod)
qntd=int(qntd)

if(cod==1):
  total = qntd*4
if(cod==2):
  total = qntd*4.5
if(cod==3):
  total = qntd*5
if(cod==4):
  total = qntd*2
if(cod==5):
  total = qntd*1.5

print("Total: R$ %.2f"%total)
