# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:29:43 2024

@author: bui vu quynh ai 
"""

nguoichoi=float(input("Nguoi chon (1.keo,2.bua,3.bao): "))
from random import randint
maychon=randint(1,3)
if maychon==1:
    print("may chon: keo")
if maychon==2:    
    print("may chon: bua")
if maychon==3:  
    print("may chon: bao")
if maychon==nguoichoi:
    print(" ket qua hoa")
elif (maychon ==1 and nguoichoi ==2) or (maychon ==2 and nguoichoi ==3) or (maychon ==3 and nguoichoi ==1):
    print (" ban thang")
else:
    print (" may thang")