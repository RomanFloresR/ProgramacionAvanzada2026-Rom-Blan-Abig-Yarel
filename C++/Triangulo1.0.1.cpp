#include <stdio.h>
// 1.0.0 – 2026-03-02 – Yareli del Carmen
// 1.0.1 - 2026-04-10 Arreglado error con la formula de área - Román

// Programa que encuentra el área de un triangulo  

int main() {
   
    float base = 10;
    float altura = 5;
    float area;

    area = (base * altura)/2;
    printf("El resultado es: %.2f\n", area);

    return 0;
}