A,B,C=input().split()
A=float(A)
B=float(B)
C=float(C)

if(A>=0 and B>=0 and C>=0):

  if(abs(B-C)<A<(B+C) and abs(B-A)<C<(B+A) and abs(A-C)<B<(A+C)):
    print("Perimetro = %.1f"%(A+B+C))
    
  else:
    print("Area = %.1f"%(((A+B)*C)/2))
