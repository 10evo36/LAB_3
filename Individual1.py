#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input("Сколько вам лет? "))
if n <= 0:
    print("Вы ввели некорректное число!")
elif n > 1 and n < 5 or n == 22 or n == 33 or n == 44:
    print("Мне", n, "года")
elif n == 1:
    print("Мне", n, "год")
else:
    print("Мне", n, "лет")
