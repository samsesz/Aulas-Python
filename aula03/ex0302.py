numero = input("Digite um numero: ")
match numero:
    case 0 | 1 | 2:
        print("Aceitavel")
    case  3 | 4 | 5:
        print("Suspender atividades do grupo 1")
    case 6 | 7:
        print("Atividades do grupo 1 e 2")
    case  8:
        print("Suspender atividades de todos os grupos")
    case _:
        print("Suspender atividades de todos os grupos")