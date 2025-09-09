frase = "Isso é uma frase de exemplo"
palavras = frase.split()
print(palavras)
#Resultado: ['Isso', 'é', 'uma', 'frase', 'de', 'exemplo']

entrada = input("Digite os elementos do vetor separados por espaços:")
vetor=[int(x) for x in entrada.split()]
print("vetor: ", vetor)