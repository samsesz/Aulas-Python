print("## Programa de emprestimos ##. \n Responda (0-Não e 1-Sim)")

negativado = int(input("Possui nome negativo?"))
if negativado == 1:
    print('Não pode realizar emprestimos')
else:
    carteiraAssinada = int(input("Possui carteira assinada ?"))

if carteiraAssinada == 0:
    print("Nao pode realizar emprestimo")
else:
    possuiCasaPropria = int(input("Possui casa propria?"))
if possuiCasaPropria == 0:
    print("Nao pode realizar o emprestimo")
else:
    print("Conceder emprestimo")