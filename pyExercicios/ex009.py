# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
print('Tabuada de multiplicação em Python!')
numero = int(input('Digite um número: '))

for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} X {resultado}')