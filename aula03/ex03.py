opcao = int(input("\n 1- Sacar \n 2- Extrato \n 3- Sair \n Escolha a opção: "))

match opcao:
    case 1:
        print("Escolheu a opção sacar")
        valor = float(input("Digite o valor do saque: R$:"))
        print(f"Sacando da sua conta o valor de {valor} ...")   
    case 2:
        print("Escolheu a opção Extrato ")  
        dias = int(input("Digite a quantidade de dias do extrato R$:"))
        print(f"Retirando o extrato de {dias} dias...")
    
    case 3:
        exit
    case _:
        print("Opção invalidə")