lista = []
cad = {}
soma = media = 0
while True:
    cad['nome'] = str(input('Nome: '))
    cad['sexo'] = str(input('Sexo: [M/F] ')).upper().split()[0]
    if cad['sexo'] not in 'MF':
        print('Erro! Por favor, digite apenas M ou F')
        cad['sexo'] = str(input('Sexo: [M/F] ')).upper().split()[0]
    cad['idade'] = int(input('Idade: '))
    soma += cad['idade']
    lista.append(cad.copy())
    cad.clear()
    exit = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if exit not in 'SN':
        print('Erro! Responda apenas S ou N.')
        exit = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if exit == 'N':
            break
media = soma/len(lista)
print(f'ao todo temos {len(lista)} pessoas cadastradas')
print(f'a média é igual a {media}')
print(f'As mulheres cadastradas foram ',end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
for p in lista:
    if p['idade'] > media:
        print(f'{p["nome"]}está acima da média com {p["idade"]} de idade')
print()
print(lista)
