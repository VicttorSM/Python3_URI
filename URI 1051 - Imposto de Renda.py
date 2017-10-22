renda=float(input())

if(0<=renda<=2000):
    print("Isento")
else:
    if(renda > 2000):
        if(renda <= 3000):
            imposto = (renda - 2000)*(8/100)
        else:
            imposto = 1000*(8/100)
    if(renda > 3000):
        if(renda <= 4500):
            imposto += (renda - 3000)*(18/100)
        else:
            imposto += (1500*(18/100))
    if(renda > 4500):
        imposto += (renda - 4500)*(28/100)

    print("R$ %.2f"%imposto)
