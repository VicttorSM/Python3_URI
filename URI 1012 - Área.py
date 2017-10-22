A,B,C=input().split()
A=float(A)
B=float(B)
C=float(C)

TRIANGULO = (A * C)/2
CIRCULO = (C**2)*3.14159
TRAPEZIO = ((A + B)*C)/2
QUADRADO = B**2
RETANGULO = A * B

print("TRIANGULO: %.3f"%TRIANGULO)
print("CIRCULO: %.3f"%CIRCULO)
print("TRAPEZIO: %.3f"%TRAPEZIO)
print("QUADRADO: %.3f"%QUADRADO)
print("RETANGULO: %.3f"%RETANGULO)
