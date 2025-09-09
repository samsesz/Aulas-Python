numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

if numero1 == numero1 or numero2 == numero3 or numero1 ==numero3:
    exit() #encerra o programa
if numero1 > numero2 and numero1 > numero3:
    print("O primeiro numero é o maior")
if numero2 > numero1 and numero2 > numero3:
    print("O segundo numero é maior")
if numero3 > numero1 and numero3 > numero2:
    print("O terceiro numero é maior")