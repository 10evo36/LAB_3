#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input("Сколько вам лет? "))
if n <= 100:
    print("Вы ввели некорректное число!")
elif n %100 > 1 and n %100 < 5 or n == 122 or n == 133 or n == 144:
    print("Мне", n, "года")
elif n == 1 or n %100 == 1:
    print("Мне", n, "год")
else:
    print("Мне", n, "лет")
