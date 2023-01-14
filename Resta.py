num = []
i = 0
fin = "s"
bucle = 0

while bucle != fin:
    valor = float(input("Ingrese valor: "))
    num.append(valor)
    if i >= 1:
        bucle = input("¿Son suficientes valores? (s/n) ")
    i = i+1

limite = i
i = 1
resta = num[0]

while i < limite:
    resta = resta - num[i]
    print("La resta es: ", resta)
    i = i+1