# -*- coding: utf-8 -*-
n = int(input())
a = bin(n)
b = a.split('0b')

_,x = b

print("%d em binario é : %s  " %(n,x))