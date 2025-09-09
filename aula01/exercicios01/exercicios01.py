m = float(input("Digite a sua altura em metros: " ))
cm = m * 100
print(cm)

deslocação = float(input("Digite a deslocação do objeto: "))
tempo = float(input("Digite a variação do tempo decorrido: "))
vm = deslocação / tempo
print(f"resultado = {vm} ")

r = input("Informe o valor do raio: ")
areaRaio = 3.14 * (r ** 2)
print(areaRaio)

base = input("Digite a base: ")
altura = input("Digite a altura: ")
area =  (base * altura)/2
print(area)

n1 = input("Digite o primeiro numero: ")
n2 = input("Digite o segundo valor: ")
soma = n1+n2
subs = n1-n2
mult = n1*n2
div = n1/n2
print(soma, subs, mult, div)

#exercicio 6
salario = input("Digite o salario atual: ")
percentual = input("Digite o percentual: ")
novo = salario * (percentual / 100)
print(novo)