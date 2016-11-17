# -*- coding: utf-8 -*-
soma = 0
qtd = 0
num = []
for i in range(10):
    n = int(input("insira um numero: "))
    num.append(n)

for i in num:
    if(i % 2 == 0):
        qtd += 1
        soma = soma + i

media = soma / qtd

print("a media dos pares é: %.2f " % (media))
