#include <stdio.h>
#include <iostream>
using namespace std;
// 1.0.0 – 2026-03-02 – Yareli del Carmen
// 1.0.1 - 2026-03-10 Arreglado error con la formula de área - Román
// 1.1.0   2026-03-11 Pide al usuario los datos de base y altura de triángulo- Abigail
// 2.0.0-  2026-03-12 Se redefinio la funcion del programa al agregarle un menu de figuras (triangulo y cuadrado) - Blanca
// Programa que encuentra el área de un triangulo  

int main() {
   int opcion;
    float base, altura, lado;
    
    cout << "1) Triangulo" << endl;
    cout << "2) Cuadrado" << endl;
    cout << "3) Salir" << endl;
    cout << "Elige una de las tres opciones que se muestran arriba : "; cin >> opcion;
    
    if(opcion == 1) {
        cout << "Base: "; cin >> base;
        cout << "Altura: "; cin >> altura;
        cout << "El area del triangulo es: " << (base * altura) / 2;
    }
    else if(opcion == 2) {
        cout << "Lado : "; cin >> lado;
        cout << "El area del cuadrado es: " << lado * lado;
    }
    else if(opcion == 3) {
        cout << "Saliendo del programa..." << endl;
    }
    else {
        cout << "\nLa opcion escrita no es valida. Por favor elige 1, 2 o 3." << endl;
    }
    
    return 0;
}
