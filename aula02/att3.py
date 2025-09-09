altura1 = float(input('Digite a estatura da 1a pessoa'))
altura2 = float(input('Digite a estatura da 2a pessoa'))
altura3 = float(input('Digite a estatura da 3a pessoa'))

if altura1 > altura2 and altura1 > altura3:
    maior = altura1
    if altura2 > altura3 :
        meio = altura2
        menor = altura3
    else:
        meio = altura3
        menor = altura2
elif altura2 > altura1 and altura2 > altura3:
    maior = altura2
    if altura1 > altura3:
        meio = altura1
        menor = altura3
    else:
        meio = altura3
        menor = altura1
else:
    maior = altura3
    if altura1 > altura2:
        meio = altura1
        menor = altura2
    else:
        meio = altura2
        menor = altura1
print(f"Pessoa 1 {maior}")
print(f"Pessoa 2 {meio}")
print(f"Pessoa 3 {menor}")