# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:49:34 2024

@author: bui vu quynh ai 23704611
"""

def giai_phuong_trinh-bac_nhat(a,b):
    if a == 0:
        if b == 0:
            return "Phuong trinh co vo so nghiem."
        else:
            return "Phuong trinh vo nghiem."
    else:
        x = -b / a
        return f" Nghiem cua phuong trinh la x = {x}"
# Vi du su dung
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
print(giai_phuong_trinh_bac_nhat(a, b))
