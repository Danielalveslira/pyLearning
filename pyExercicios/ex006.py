# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número: '))

print('Numero: {}, Dobro: {}, Triplo: {} e Raiz Quadrada: {}.'.format(numero, (numero + numero), (numero * 3), (pow(numero, 0.5))))