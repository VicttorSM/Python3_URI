S=1; cont=1

for i in range(19):
    cont*=2
    S+=(3+(i*2))/(cont)
print("%.2f"%S)
