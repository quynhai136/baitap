# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:59:25 2024

@author: bui vu quynh ai
"""

import math 
a = float(input("Nhap gia tri a: "))
b = float(input("Nhap gia tri b: "))
c = float(input("Nhap gia tri c: "))
if a + b > c and a + c > b and b + c >a:
    print ("a, b, c la ba canh cua mot tam giac")
    if a ==b == c:
        print("Tam giac deu")
    elif (math.isclose(a**2 +b**2, c**2)   or
        math.isclose(a**2 +c**2, b**2) or
        math.isclose(b**2 +c**2, a**2)):
            print ("Tam giac vuong")
    elif a ==b or b ==c or a == c:
        print("Tam giac can")
    else:
        print("Tam giac thuong")
else:
    print("a, b, c khong phai la canh cua mot tam giac")