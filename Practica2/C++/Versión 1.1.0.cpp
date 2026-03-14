/* c_no_opt.cX
   Versión: 1.0.0
   El código en C itera los enteros desde 2 hasta N, para cada número prueba divisores 
   mediante un bucle while para determinar si es primo, marca el resultado con una variable
   booleana, y cuando detecta un primo actualiza el contador total, suma su valor a un acumulador 
   y clasifica si es par o impar; emplea for, while e if/else anidados para la generación de 
   candidatos, la verificación de divisores y la actualización de contadores y suma.
/* En esta versión 1.1.0 se elimina el while y se reemplaza por un for más compacto, usamos una nueva función
el operador ternario que funciona como un for pero más compacto lo que permite mayor eficiencia
además eliminamos las operaciones y variables redundantes haciendo del código mucho más compacto en comparación a un principio

*/

// Versión: 1.1.0 Se convirtió en un código más eficiente y compacto 


#include <stdio.h>
#include <stdlib.h>

int main() {
    //Variables principales, contadoras y acumuladoras
    long long suma_primos = 0;
    int primos_pares = 0,primos_impares = 0, count_primos = 0,N = 1000 ;
   

               	//// MOD:V
               	//Recorremos todos los numeros desde 2 hasta N
    for (int m = 2; m <= N; m++) {   // cambio se simplifico for 
        int es_primo = 1; /* asumimos primo hasta demostrar lo contrario */
        // Eliminamos las redudancias que no aportaban nada 
// Eliminamos el while y lo simplificamos en un for más compacto
        for (int d = 2; d * d <= m; d++) {
            if (m % d == 0) { es_primo = 0; // si encontramos divisor, no es primo
                break;        // salimos del ciclo inmediatamente
        // Si el número es primo, actualizamos el sistema de acum
        }
        if (es_primo) {
            count_primos++;
            suma_primos += m;
            (m % 2 == 0 ? primos_pares : primos_impares)++; //El operador ternario en C es una forma compacta de escribir una condición
             // si m es par → incrementa primos_pares
            // si m es impar → incrementa primos_impares

        }
    }

    printf("Primos encontrados: %d\n", count_primos);
    printf("Suma de primos: %lld\n", suma_primos);
    printf("Primos pares: %d\n", primos_pares);
    printf("Primos impares: %d\n", primos_impares);

    return 0;
}
