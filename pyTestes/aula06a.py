n1 = int(input('Digite um valor: ')) # Valor inteiro
n2 = int(input('Digite outro: '))
soma = n1 + n2
print('A soma entre {0} e {1} é igual a: {2}'.format(n1, n2, soma))
# print('A soma entre {} e {} é igual a: {}'.format(n1, n2, soma))
print('A soma é: {}'.format(n1 + n2))

# Tipos de dados booleanos:
n = float(input('Digite um número: '))
print('Número em float: {}'.format(n))
# Verificando se um dado é número:
isNumber = input('Digite algo: ')
print(isNumber.isnumeric()) # Return true or false depending on the input
print(isNumber.isalpha()) # Cheking if is a letter
print(isNumber.isalnum()) # Cheking if is a number