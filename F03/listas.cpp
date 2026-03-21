/*


El objetivo es mostrar cómo almacenar, organizar y procesar datos
de una manera similar a como se haría en C, pero usando las
estructuras de alto nivel de C++.
*/
// Listas
//Autor: Abigail Morales Carmona
// Versión 1.00


#include <iostream>
#include <vector>

using namespace std;

int main() {
    // -----------------------------
    // 1. VECTORES (equivalente a listas)
    // -----------------------------
    vector<int> numeros = {10, 20, 30, 40, 50}; // Lista modificable

    // Agregamos un número al final
    numeros.push_back(60); // Ahora el vector es [10,20,30,40,50,60]

    cout << "Contenido del vector 'numeros':" << endl;
    for (int n : numeros) {
        cout << "- " << n << endl;
    }

    
    return 0;
}