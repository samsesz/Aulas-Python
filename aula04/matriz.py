matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Elemento na primeira linha e coluna:", matriz[0][0])
print("Elemento na segunda linha e coluna:", matriz[1][2])
print("Elemento na terceira linha e coluna:", matriz[2][1])

print("Matriz:")
for linha in matriz:
    print(linha)

linhas = int(input("Digite o numero de linhas da matriz: "))
colunas = int(input("Digite o numero de colunas da matriz: "))

matriz_numeros = []
for i in range(linhas):
    linha = []
    matriz_numeros.append(linha)
    #for j in range(colunas):
       # numero = float(input(f"Digite o numero para a posição ({i}, {j})"))
              #linha.append(numero) novo registro