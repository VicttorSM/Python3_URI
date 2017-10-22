N=[]
for i in range(20):
    A=input()
    N+=[A]

for i in range(10):
    temporário=N[i]
    N[i]=N[19-i]
    N[19-i]=temporário


for i in range(20):
    print("N[%i] ="%(i),N[i])
