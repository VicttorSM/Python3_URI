contFatorialN=0

N=int(input())
n=N-1

while(n>1):
    if(n==N-1):
        contFatorialN=N*n
    else:
        contFatorialN*=n
    n-=1


print(contFatorialN)
