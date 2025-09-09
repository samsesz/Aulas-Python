matriz = []
maiorq10 = 0

#matriz 4x4
for i in range(4):
    linha = []
    matriz.append(linha)
    for i in range(4):
        numero = int(input(f"Digite um valor inteiro {i+1},{j+1}:"))
        linha.append(numero)
        if numero > 10 :
            maiorq10 += 1
for i in range (4):
    print(matriz[i])

print(matriz)
print(f"Existem {maiorq10} numero maiores que 10")