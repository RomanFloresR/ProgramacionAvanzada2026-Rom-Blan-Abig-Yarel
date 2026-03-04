# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 08:47:51 2026

@author: abiga

programa que se encarga de sacarle el area a un triangulo 
"""

#Versión 1.0.0 en esta versión se encuentra un error.
#Version 1.0.1 correccin de formula, descripcion agregada - Blanca
#Version 1.1.0 pedir datos al usuario para el calculo - Yareli  
#Version 1.2.0 Definición de funciones. Menu para volver a calcular -Román

def Calc_Area_Triangulo():
    base= float(input("ingresa la base: "))
    altura= float (input ("ingresa la altura: "))
    area=(base*altura)/2
    print("El area es igual a ", area)

K=1

while K==1:
    Calc_Area_Triangulo()
    K=float(input("Volver a realizar operación ingrese 1, Salir ingrese cualquier otro: "))


    