#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = int(input("Введите a "))
b = int(input("Введите b "))
if a>20 and b > 20 and a<100 and b < 100 and a%3==0 and b %3 == 0:
   S=a+b
   print("Сумма чисел равна" ,S )
else:
   print("Числа не подходят по условию!")
