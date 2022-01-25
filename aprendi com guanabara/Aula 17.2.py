teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste[:])
print(galera)
teste[0] = "Maria"
teste[1] = 22
galera.append(teste)
print(galera)

turma = [['Joao', 19], ['Ana', 33], ['Maria', 45], ['Joaquim', 13]]
print(turma)
print(turma[0])
print(turma[0][0])
print(turma[2][1])
for p in turma:
    print(p)
for p in turma:
    print(p[1])
for p in turma:
    print(f'{p[0]} tem {p[1]} anos de idade. ')

cliente = list()
dado = list()
for c in range(4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    cliente.append(dado[:])
    dado.clear()
print(cliente)
print(dado)
for a in cliente:
    if a[1] >= 21:
        print(f'{a[0]} é maior de idade.')
    else:
        print(f'{a[0]} é menor de idade.')
