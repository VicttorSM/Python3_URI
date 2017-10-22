I=int(1); J=int(7); N=0

while not(I>9 and J>13):
    print("I=%i J=%i"%(I,J))
    J-=1
    if(J==5+(N/2)):
        print("I=%i J=%i"%(I,J))
        J+=4
        N+=4
        I+=2
