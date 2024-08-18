# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:13:21 2024

@author: bui vu quynh ai 23704611
"""

# Nhap diem GPA tu ban phim
gpa = float(input("Nhap diem trung binh (GPA): "))

#Xac dinh va thong bao ket qua xep hang cua hoc luc
if gpa < 3.5:
    print("Hoc luc kem")
elif 3.5 <= gpa < 5.0:
    print("Hoc luc yeu")
elif 5.0 <= gpa < 7.0:
    print("Hoc luc Trung Binh")
elif 8.0 <= gpa < 9.0:
    print("Hoc luc Gioi")
elif 9.0 <= gpa <=10:
    print("Hoc luc Xuat sac")
else:
    print("Diem GPA khong hop le. Vui long nhap diem tu 0 den 10.")