tamanho = int(input("Digite o tamanho do vetor:"))
vetor = []

for i in range(tamanho):
    num = int(input(f"Digite o {i} inteiro:"))
    vetor.append(num)

print(vetor)