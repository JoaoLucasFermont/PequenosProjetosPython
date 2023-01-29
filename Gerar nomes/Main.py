from random import randrange

print('[1] Sexo Masculino \n[2] Sexo Feminino')
Sexoimput = input('digite o sexo para gerar o nome:  ')

listamasc = []
listafem = []
listasobrenomes = []

with open("NomesMasc.txt", "r") as arquivo:
    for nomes in arquivo:
        listamasc.append(nomes.strip())

with open("NomesFem.txt", "r") as arquivo:
    for nomes in arquivo:
        listafem.append(nomes.strip())

with open("sobrenomes.txt", "r") as arquivo:
    for nomes in arquivo:
        listasobrenomes.append(nomes.strip())


if Sexoimput == '1':
    print(f'O nome Gerado foi: {listamasc[randrange(0,99)]} {listasobrenomes[randrange(0,99)]}')

elif Sexoimput == '2':
    print(f'O nome Gerado foi: {listafem[randrange(0, 99)]} {listasobrenomes[randrange(0, 99)]}')

else:
    print(f'Erro')











