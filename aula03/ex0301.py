letra = input("Digite uma letra")

match letra:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("Voce digitou uma vogal!")
    case _:
        print("Voce digitou uma consoante!")
    