I=int(1); J=int(7)
while not(I==11 and J==7):
    print("I=%i J=%i"%(I,J))
    J-=1
    if(J==5):
        print("I=%i J=%i"%(I,J))
        I+=2
        J=7
