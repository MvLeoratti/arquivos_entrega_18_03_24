# -*- coding: utf-8 -*-
"""lista de For.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18V13UFiOqQaCAK7FtDy3QXWz0uKCJ-u9
"""

x=int(input("Digite um valor: "))
for i in range(x):
  R = i*3
  print(f"O valor e {R}")

for count in range(1, 6):
  numero = int(input(f"Digite um numero: "))
  if (numero > count ):
    print(f"O maior numero e {numero}")

for count1 in range(1000,2001):
  if (count1 % 11 ==2):
    print(f"{count1}")

soma = int()
for i in range(1,6):
  n = int(input("Digite um numero"))
  soma+=n
  media = soma /(i)
print(f"A media de {i} e: {media}")
print(f"A Soma é :{soma}")

numero = int(input("Digite o numero da Tabuada: "))
for i in range(1,11):
  calc = i * numero
  print(f"{i} x {numero} = {calc}")

for i in range(1,11):
  numero = i
  for s in range(1,11):
    calc = s * numero
    print(f"{s} x {numero} = {calc}")

for i in range(1,21):
  print(f"{i}")
print(list(range(1,21)))

for i in range(1,51):
  if i%2!=0:
    print(f"{i}")

num1 = int(input("Digite um numero interiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))

for p in range(1,5):
  if (p>=num1) and (p<num2):
    print(f"{p}")

fat_lojaA = float(input("Digite o valor do faturamento da Loja A: "))
fat_lojaB = float(input("Digite o valor do faturamento da Loja B: "))


if fat_lojaA>=54000 and fat_lojaA>fat_lojaB:
  print(f"{fat_lojaA}")
else:
  print("Valor fora do parametro estimado!!")

num=int(input("Digite um numero inteiro"))

for i in range(1,11):
  if (num%2==0):
    count+=1
  else:
    count1+=1
print(f"A quantidade de numeros Pares e: {count}")
print(f"A quantidade de numeros Impares e: {count1}")

salario = float(input("Digite o salario incial do funcionario: "))
percentual = 0.015
for i in range(1996,2025):
  aumento = salario * percentual
  salario+=aumento
  percentual*=2
  aumento = salario_atual *2
  print(f"O Salario em {i} = {salario_atual}")



for i in enumerate(iter(bool,True),start=0):
  nota=int(input("Digite a Nota: "))
  if nota>=0 and nota<=10:
    print(f"Nota Valida e {nota} ")
    break
  else:
    print("Nota Invalida")

