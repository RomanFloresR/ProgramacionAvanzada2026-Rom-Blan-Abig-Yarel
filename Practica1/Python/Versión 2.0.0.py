# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 08:47:51 2026

@author: abiga

programa que se encarga de sacarle el area a un triangulo o un cuadrado.
"""

#Versión 1.0.0 en esta versión se encuentra un error.
#Version 1.0.1 correccin de formula, descripcion agregada - Blanca
#Version 1.1.0 pedir datos al usuario para el calculo - Yareli  
#Version 1.2.0 Definición de funciones. Menu para volver a calcular -Román
#Version 2.0.0 Se redefinio la funcion del programa, se agrego la funcion del cuadrado 
#y se agrego un menu de figuras para el usuario. - Blanca

def Calc_Area_Triangulo():
    base= float(input("ingresa la base: "))
    altura= float (input ("ingresa la altura: "))
    area=(base*altura)/2
    print("El area es igual a ", area)
    
def Calc_Area_Cuadrado():
    base= float(input("ingresa la base:"))
    area=(base*base)
    print("El area es igual a ", area)
    

K=1

while K==1:
    figura= int(input("ingresa la figura que quieres: \n 1) Triangulo \n 2) Cuadrado \n -", ))
    if figura==1:
        Calc_Area_Triangulo() 
    elif figura==2:
        Calc_Area_Cuadrado()
    else:
        print("No es un numero valido, ingrese un numero de la lista")
    K=float(input("Volver a realizar operación ingrese 1, Salir ingrese cualquier otro: "))