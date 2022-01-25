frase = str('Curso em Video Python')
frase2 = str('  Aprenda Python  ')

# apresenta os caracteres no intervalo, sempre entre [ ]
print(frase[3],'   letra especifica')
print(frase[7])

# contagem dos caracteres começa do 0 até o último, no caso de 0 a 20, o último do intervalo dado é ignorado
print(frase[9:20])

# se não tem onde começa, ele começa do caractere 0
print(frase[:5])

# indiquei início e não sei o final.. então vai até o final
print(frase[15:])

# Começa do 9 até o final, pula de 3 em 3
print(frase[9::3])

# comprimento da frase
print(len(frase), '    comprimento')
print(len(frase2))
print(len(frase2.strip()))

# contar quantas vezes aparece o caractere dado, entre intervalo ou não
print(frase.count('o'), '    contador de letras')
print(frase.count('o', 0, 13))

# encontrou a sequencia dada, sem aparição retorna negativo
print(frase.find('deo'))
print(frase.find('android'))

# Operador de análise, retorna verdadeiro ou falso
print('Curso' in frase)

# Substituir
print(frase.replace('Python', 'Android'), '     Substituir')

# Maiúscula, minuscula, capitalizado, todas primeiras maiusculas
print(frase.upper(), '      maiusculas minusculas ')
print(frase.lower())
print(frase.capitalize())
print(frase.title())

# Remover espaços, espaços à direita, espaços à esquerda
print(frase2, '     remove os espaços antes e depois')
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

# Dividir a frase em espaços, juntar as letras com o caractere indicado
print(frase.split())
print('-'.join(frase))
