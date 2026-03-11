#include <stdio.h>
#include <iostream>
using namespace std;
// 1.0.0 – 2026-03-02 – Yareli del Carmen
// 1.0.1 - 2026-03-10 Arreglado error con la formula de área - Román
// 1.1.0   2026-03-11 Pide al usuario los datos de base y altura de triángulo- Abigail
// Programa que encuentra el área de un triangulo  

int main() {
   float base, altura;
    cout<<"Base: "; cin >> base;
    cout<<"Altura: "; cin >> altura;  
     cout<<"El area del triángulo es: "<< (base*altura)/2; 
    return 0;}
