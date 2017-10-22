maior=0
for i in range(100):
    N=int(input())
    if(N>maior):
        maior=N
        pos=i+1
print(maior)
print(pos)
