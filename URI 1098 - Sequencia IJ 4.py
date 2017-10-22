I=float(0); J=float(1); N=0

while True:
    if(I%1==0):
        print("I=%i J=%i"%(I,J))
    else:
        print("I=%.1f J=%.1f"%(I,J))
    
    J+=1
    
    if(J==(3.0+I)):
        if(I%1==0):
            print("I=%i J=%i"%(I,J))
        else:
            print("I=%.1f J=%.1f"%(I,J))
        if(I>=2.0 and J>=5.0):
            break
        N=int(N)
        N+=1
        J=int(J)
        I=int(I)
        I=float(0.2*N)
        J=float((1+(0.2*N)))
