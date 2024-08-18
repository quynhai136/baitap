# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:53:58 2024

@author: bui vu quynh ai
"""

import math
a = float(input("Nhap a:"))
b = float(input("Nhap b:"))
c = float(input("Nhap c:"))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh vo so nghiem!")
        else:
            print("Phuong trinh vo nghiem!")
    else:
        x = -c/b
        print("Phuong trinh co 1 nghiem x =", x)
else:
    delta = b ** 2 - 4 *a * c
if delta < 0:
    print("Phuong trinh vo nghiem!")
elif delta == 0:
    x = -b / (2 * a)
    print("Phuong trinh co 1 nghiem kep m", x)
else:
    print("Phuong trinh co 2 nghiem phan biet!")
    x1= (-b + math.sprt(delta)) / (2 * a)
    x2= (-b - math.sprt(delta)) / (2 * a)
    print("x1 = ", x1)
    print("x2 = ", x2)  
    