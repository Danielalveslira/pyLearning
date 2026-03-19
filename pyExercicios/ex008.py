# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metro = float(input('Digite um valor em metros: '))

centimetros = metro * 100
milimetros = metro * 1000

print(f'Metros: {metro}, em centimetro: {centimetros}, em milimetro: {milimetros}')