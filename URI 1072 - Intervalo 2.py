contIn=0; contOut=0

N=int(input())
for i in range(N):
    X=int(input())
    if(10<=X<=20):
        contIn+=1
    else:
        contOut+=1

print(contIn,"in")
print(contOut,"out")
